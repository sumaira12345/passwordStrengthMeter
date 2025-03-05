import streamlit as st
import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r"[A-Z]", password))
    lowercase_criteria = bool(re.search(r"[a-z]", password))
    digit_criteria = bool(re.search(r"[0-9]", password))
    special_char_criteria = bool(re.search(r"[@$!%*?&#]", password))
    
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])
    
    if score == 5:
        return "Strong", "#2ECC71"  # Green
    elif score >= 3:
        return "Medium", "#F39C12"  # Orange
    else:
        return "Weak", "#E74C3C"  # Red

def ai_suggestion(password):
    suggestions = {
        "Weak": "Your password is weak. Consider adding uppercase letters, numbers, and special characters to make it stronger.",
        "Medium": "Your password is decent but could be stronger. Try increasing the length and adding more complexity.",
        "Strong": "Great job! Your password is strong and secure. Keep it safe."
    }
    strength, color = check_password_strength(password)
    return strength, suggestions[strength], color

def main():
    st.set_page_config(page_title="Password Strength Meter", layout="centered")
    
    st.title("🔒 Password Strength Meter")
    st.write("Enter a password to check its strength.")
    
    password = st.text_input("Password", type="password")
    
    if st.button("Check Strength"):
        if password:
            strength, suggestion, color = ai_suggestion(password)
            st.markdown(f"<h3 style='color: {color};'>Strength: {strength}</h3>", unsafe_allow_html=True)
            st.write(suggestion)
        else:
            st.warning("Please enter a password to check its strength.")

if __name__ == "__main__":
    main()
