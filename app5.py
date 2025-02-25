'''
Version control - Github.com
Deploy Generative AI app on Cloud web server

Steps
1- https://github.com/ (sign up and login)
'''

import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyBBZTmDHnqAP6p2gKqTmSfv6bbNf2gYhXM")

model = genai.GenerativeModel("gemini-1.5-flash")

st.title("Code Review ")
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