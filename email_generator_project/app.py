
import streamlit as st

def generate_email(job_title, job_description, your_name, phone, email, skills, company_name, manager_name):
    # Process skills into a nicer sentence
    skill_list = [s.strip() for s in skills.split(",")]
    skill_sentence = ""
    if len(skill_list) > 1:
        skill_sentence = ", ".join(skill_list[:-1]) + " and " + skill_list[-1]
    else:
        skill_sentence = skills

    # Shorten job description to key points (first 3 lines or so)
    key_points = job_description.strip().split("\n")
    key_points = [point.strip() for point in key_points if point.strip() != ""]
    key_points = key_points[:3]
    key_points_sentence = " ".join(key_points)

    # Compose a stronger opening and value proposition
    opening = f"Your {job_title} position at {company_name} immediately caught my attention because of its focus on {key_points_sentence.lower()}."
    
    value_prop = f"My experience with {skill_sentence} has prepared me to effectively contribute to your team by delivering actionable insights and supporting data-driven decisions."

    # Personalize greeting
    if manager_name:
        greeting = f"Dear {manager_name},"
    else:
        greeting = "Dear Hiring Manager,"

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

# Streamlit UI starts here
st.title("AI Email Generator for Job Applications")

job_title = st.text_input("Enter Job Title")
job_description = st.text_area("Paste Job Description")
company_name = st.text_input("Company Name (optional)")
manager_name = st.text_input("Hiring Manager's Name (optional)")
your_name = st.text_input("Your Full Name", "Ayushi Jaiswal")
phone = st.text_input("Your Phone Number", "+91-XXXXXXXXXX")
email = st.text_input("Your Email", "your-email@example.com")
skills = st.text_input("Your Skills (comma separated)", "Python, C++, SQL, Excel, Power BI, Django, MySQL")

if st.button("Generate Email"):
    if job_title and job_description:
        email_body = generate_email(job_title, job_description, your_name, phone, email, skills, company_name, manager_name)
        st.subheader("Generated Email:")
        st.code(email_body)
    else:
        st.error("Please enter both Job Title and Job Description.")
