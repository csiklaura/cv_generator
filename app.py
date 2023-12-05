import streamlit as st
import os
from cv_creators.millenial_grey import create_cv as millenial_grey_cv
from cv_creators.fun_grey_green import create_cv as fun_grey_green_cv


TEMPLATES = {
    "Millenial Grey Modern": millenial_grey_cv,
    "Fun Grey Green Modern": fun_grey_green_cv,
}


# Streamlit app
def main():
    st.title('CV Generator')

    selected_template = st.selectbox('Choose a CV template', TEMPLATES)

    with st.form("user_info_form"):
        name = st.text_input("Name")
        title = st.text_input("Title")
        phone = st.text_input("Phone")
        email = st.text_input("Email")
        profile_summary = st.text_area("Profile Summary")
        education = st.text_area("Education")
        experience = st.text_area("Experience")
        skills = st.text_area("Skills")
        certifications = st.text_area("Certifications")
        language = st.text_area("Language")
        expertise = st.text_area("Expertise")

        submitted = st.form_submit_button("Generate CV")

        if submitted:
            user_info = {
                "name": name,
                "title": title,
                "phone": phone,
                "email": email,
                "profile_summary": profile_summary,
                "education": education,
                "experience": experience,
                "skills": skills,
                "certifications": certifications,
                "language": language,
                "expertise": expertise,
            }

            # Generate CV
            pdf = TEMPLATES[selected_template](user_info=user_info)
            st.session_state['pdf'] = pdf
            st.success('CV generated! Scroll down to download.')

    if 'pdf' in st.session_state:
        st.download_button(label="Download CV as PDF",
                           data=st.session_state['pdf'],
                           file_name=f"{selected_template} CV.pdf",
                           mime='application/pdf')


if __name__ == "__main__":
    main()
