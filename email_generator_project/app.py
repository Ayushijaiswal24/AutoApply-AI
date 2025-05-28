import streamlit as st
import re

# Page configuration
st.set_page_config(page_title="AutoApply AI", layout="centered")

# Custom baby pink theme
st.markdown(""" 
    <style>
    .stApp {
        background-color: #ffe6f0;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #cc0066;
        text-align: center;
    }
    .stTextInput > div > input, .stTextArea > div > textarea {
        border: 2px solid #ff66b2;
        border-radius: 10px;
        padding: 8px;
        background-color: #fff0f5;
        font-size: 16px;
    }
    .stButton > button {
        background-color: #ff66b2;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        font-size: 16px;
        padding: 10px 20px;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Validation functions
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_valid_phone(phone):
    # Indian phone number format (10 digits starting with 6-9)
    return re.match(r"^[6-9]\d{9}$", phone)

def generate_email(job_title, job_description, your_name, phone, email, skills, company_name, manager_name):
    skill_list = [s.strip() for s in skills.split(",")]
    skill_sentence = ""
    if len(skill_list) > 1:
        skill_sentence = ", ".join(skill_list[:-1]) + " and " + skill_list[-1]
    else:
        skill_sentence = skills

    key_points = job_description.strip().split("\n")
    key_points = [point.strip() for point in key_points if point.strip() != ""]
    key_points = key_points[:3]
    key_points_sentence = " ".join(key_points)

    opening = f"Your {job_title} position at {company_name} immediately caught my attention because of its focus on {key_points_sentence.lower()}."
    value_prop = f"My experience with {skill_sentence} has prepared me to effectively contribute to your team by delivering actionable insights and supporting data-driven decisions."

    greeting = f"Dear {manager_name}," if manager_name else "Dear Hiring Manager,"

    email_text = f"""
Subject: Application for the {job_title} Position – {your_name}

{greeting}

{opening}

{value_prop}

I am excited about the opportunity to bring my skills and enthusiasm to {company_name}.

Please find my resume attached for your review. I look forward to the possibility of discussing how I can add value to your organization.

Thank you for considering my application.

Best regards,  
{your_name}  
📞 Phone: {phone}  
✉️ Email: {email}
"""
    return email_text

st.title("AI Email Generator for Job Applications")

# Inputs
job_title = st.text_input("Job Title *")
job_description = st.text_area("Job Description *")
company_name = st.text_input("Company Name (optional)")
manager_name = st.text_input("Hiring Manager's Name (optional)")
your_name = st.text_input("Your Full Name *")
phone = st.text_input("Your Phone Number (10 digits) *")
email = st.text_input("Your Email *")
skills = st.text_input("Your Skills (comma separated)", "Python, C++, SQL, Excel, Power BI, Django, MySQL")

if st.button("Generate Email"):
    # Check mandatory fields
    if not job_title.strip():
        st.error("Job Title is required.")
    elif not job_description.strip():
        st.error("Job Description is required.")
    elif not your_name.strip():
        st.error("Your Full Name is required.")
    elif not email.strip():
        st.error("Your Email is required.")
    elif not phone.strip():
        st.error("Your Phone Number is required.")
    # Validate email and phone
    elif not is_valid_email(email.strip()):
        st.error("Please enter a valid email address.")
    elif not is_valid_phone(phone.strip()):
        st.error("Please enter a valid 10-digit Indian phone number starting with 6-9.")
    else:
        email_body = generate_email(job_title.strip(), job_description.strip(), your_name.strip(),
                                    phone.strip(), email.strip(), skills.strip(),
                                    company_name.strip(), manager_name.strip())
        st.subheader("Generated Email:")
        st.code(email_body)
