'''
Version Control - GitHub.com
Deploy Generative AI app on Cloud Web Server


What is GitHub.com?

1. Sign-up in GitHub website - https://github.com/
2. Login in GitHUb website - https://github.com/

'''


import streamlit as st
import google.generativeai as genai


# Configure Generative AI (Ensure API key is set securely)
#api_key = st.secrets["AIzaSyBW0FGG-5hw41OV-XFniCfkscT3lqIcJ0w"]  # Recommended way to store API keys securely
genai.configure(api_key="AIzaSyBW0FGG-5hw41OV-XFniCfkscT3lqIcJ0w")

# Initialize model
model = genai.GenerativeModel("gemini-1.5-flash")

# Code Review Section
st.subheader("Code Review")

code = st.text_area("Enter your programming code to rectify the error:")

if st.button("Code Review"):
    if code.strip():
        response = model.generate_content(f"""
        Rectify the following code:
        {code}

        1. **Code Review** - Provide an overall assessment.
        2. **Error Explanation** - Highlight mistakes and why they occur.
        3. **Fixing Issues** - Suggest changes and where to apply them.
        4. **Corrected Code** - Provide a fully corrected version.
        5. **Optimization Tips** - Suggest ways to improve efficiency.

        Format the response in an easy-to-understand manner with **bold key points**.
        """)
        st.write(response.text)
    else:
        st.warning("Please enter some code before submitting.")
