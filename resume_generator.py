import random


def generate_professional_experience(experience, qualification, achievements, length):
    paragraph = f"Professional with {experience} years of experience in {qualification}. "
    paragraph += f"Achieved {achievements}. "
    paragraph += "Skilled in various aspects of the field."
    if len(paragraph.split()) > length:
        paragraph = ' '.join(paragraph.split()[:length])
    return paragraph

def generate_work_history(locations, roles, achievements):
    history = []
    for loc, role, achieve in zip(locations, roles, achievements):
        history.append(f"{loc}: {role}. Achievements: {achieve}")
    return '\n'.join(history)

def generate_contact(email, phone, address):
    return f"Contact Details:\nEmail: {email}\nPhone: {phone}\nAddress: {address}"

def generate_skills(skills):
    return f"Skills: {', '.join(skills)}"

def generate_education(schools, years, degrees):
    education = []
    for school, year, degree in zip(schools, years, degrees):
        education.append(f"{school} ({year}): {degree}")
    return '\n'.join(education)

def generate_personal_info(name, age, gender):
    return f"Name: {name}\nAge: {age}\nGender: {gender}"


#PRevious vers
# def generate_resume(template, details):
#     if template == "Basic":
#         professional_exp = generate_professional_experience(details["experience"], details["qualification"], details["achievements"], 50)
#         work_history = generate_work_history(details["locations"], details["roles"], details["achievements"])
#         contact = generate_contact(details["email"], details["phone"], details["address"])
#         skills = generate_skills(details["skills"])
#         education = generate_education(details["schools"], details["years"], details["degrees"])
#         personal_info = generate_personal_info(details["name"], details["age"], details["gender"])
#
#         resume = f"{personal_info}\n\n{professional_exp}\n\n{work_history}\n\n{contact}\n\n{skills}\n\n{education}"
#         return resume
#     else:
#         return "Resume template not supported."



def generate_resume(details):
    # Define multiple templates
    templates = {
        "Template 1:": {
            "professional_exp": f"I am a {details['qualification']} with {details['experience']} years of experience. "
                                f"My achievements include {details['achievements']}. I have a proven track record of "
                                f"success in various projects and initiatives. I have led teams to deliver complex "
                                f"solutions on time and within budget. My expertise in the field has been honed through "
                                f"years of practical experience and continuous learning. I am committed to professional "
                                f"excellence and strive to exceed expectations in all my endeavors.",
            "work_history": generate_work_history(details['locations'], details['roles'], details['achievements']),
            "contact": f"Contact Details:\nEmail: {details['email']}\nPhone: {details['phone']}\nAddress: {details['address']}",
            "skills": f"Skills: {', '.join(details['skills'])}",
            "education": generate_education(details['schools'], details['years'], details['degrees']),
            "personal_info": f"Name: {details['name']}\nAge: {details['age']}\nGender: {details['gender']}"
        },
        "Template 2:": {
            "professional_exp": f"I bring {details['experience']} years of expertise in {details['qualification']} with notable "
                                f"achievements in {details['achievements']}. My career journey has been defined by my ability "
                                f"to adapt to new challenges and continuously improve my skill set. I thrive in dynamic environments "
                                f"and am always eager to take on new opportunities that allow me to grow both professionally and personally. "
                                f"My innovative approach and dedication to excellence have been key drivers of my success.",
            "work_history": generate_work_history(details['locations'], details['roles'], details['achievements']),
            "contact": f"Get in touch:\nEmail: {details['email']}\nPhone: {details['phone']}\nLocation: {details['address']}",
            "skills": f"My skills include: {', '.join(details['skills'])}",
            "education": generate_education(details['schools'], details['years'], details['degrees']),
            "personal_info": f"Name: {details['name']}\nAge: {details['age']}\nGender: {details['gender']}"
        },
        "Template 3:": {
            "professional_exp": f"I am a creative {details['qualification']} with a passion for {details['achievements']}. "
                                f"With {details['experience']} years of experience, I have a proven track record of success. "
                                f"My work is characterized by my innovative thinking and my ability to bring new ideas to life. "
                                f"I am always looking for new ways to push the boundaries and create work that is both impactful "
                                f"and meaningful. My commitment to my craft is evident in everything I do, and I am always striving "
                                f"to improve and grow as a professional.",
            "work_history": generate_work_history(details['locations'], details['roles'], details['achievements']),
            "contact": f"Reach out:\nEmail: {details['email']}\nPhone: {details['phone']}\nHome: {details['address']}",
            "skills": f"Key skills: {', '.join(details['skills'])}",
            "education": generate_education(details['schools'], details['years'], details['degrees']),
            "personal_info": f"Name: {details['name']}\nAge: {details['age']}\nGender: {details['gender']}"
        },
        "Template 4:": {
            "professional_exp": f"I am a tech-savvy {details['qualification']} with {details['experience']} years of hands-on experience. "
                                f"My achievements include {details['achievements']}. I have a deep understanding of the latest technologies "
                                f"and how they can be leveraged to drive business success. My technical skills are complemented by my ability "
                                f"to communicate complex ideas clearly and effectively. I am always looking for new ways to innovate and stay "
                                f"ahead of the curve in the fast-paced world of technology.",
            "work_history": generate_work_history(details['locations'], details['roles'], details['achievements']),
            "contact": f"Connect with me:\nEmail: {details['email']}\nPhone: {details['phone']}\nLocation: {details['address']}",
            "skills": f"Key skills: {', '.join(details['skills'])}",
            "education": generate_education(details['schools'], details['years'], details['degrees']),
            "personal_info": f"Name: {details['name']}\nAge: {details['age']}\nGender: {details['gender']}"
        },
        "Template 5:": {
            "professional_exp": f"{details['experience']} years in {details['qualification']}. Achievements: {details['achievements']}. "
                                f"My career has been marked by my ability to deliver results and drive change. I am known for my "
                                f"strategic thinking and my ability to execute on complex projects. My focus is always on achieving "
                                f"the best possible outcomes and making a positive impact. I am a results-oriented professional who is "
                                f"always looking for new ways to improve and grow.",
            "work_history": generate_work_history(details['locations'], details['roles'], details['achievements']),
            "contact": f"Email: {details['email']}\nPhone: {details['phone']}\nAddress: {details['address']}",
            "skills": f"Skills: {', '.join(details['skills'])}",
            "education": generate_education(details['schools'], details['years'], details['degrees']),
            "personal_info": f"Name: {details['name']}\nAge: {details['age']}\nGender: {details['gender']}"
        },
        "Template 6:": {
            "professional_exp": f"I am an experienced {details['qualification']} with {details['experience']} years in the industry. "
                                f"My accomplishments include {details['achievements']}. I have a proven track record of success and am "
                                f"committed to professional excellence. My experience has equipped me with the skills and knowledge needed "
                                f"to excel in my field. I am dedicated to continuous learning and always strive to stay ahead of industry trends.",
            "work_history": generate_work_history(details['locations'], details['roles'], details['achievements']),
            "contact": f"Contact:\nEmail: {details['email']}\nPhone: {details['phone']}\nLocation: {details['address']}",
            "skills": f"Key Skills: {', '.join(details['skills'])}",
            "education": generate_education(details['schools'], details['years'], details['degrees']),
            "personal_info": f"Name: {details['name']}\nAge: {details['age']}\nGender: {details['gender']}"
        },
        "Template 7: ": {
            "professional_exp": f"I am a results-driven {details['qualification']} with {details['experience']} years of experience in driving "
                                f"revenue growth and developing impactful marketing strategies. My accomplishments include {details['achievements']}. "
                                f"I am passionate about using my skills to create value and drive business success. My expertise in marketing and "
                                f"sales has been honed through years of practical experience and continuous learning.",
            "work_history": generate_work_history(details['locations'], details['roles'], details['achievements']),
            "contact": f"Contact Me:\nEmail: {details['email']}\nPhone: {details['phone']}\nLocation: {details['address']}",
            "skills": f"Key Skills: {', '.join(details['skills'])}",
            "education": generate_education(details['schools'], details['years'], details['degrees']),
            "personal_info": f"Name: {details['name']}\nAge: {details['age']}\nGender: {details['gender']}"
        },
        "Template 8: ": {
            "professional_exp": f"With over {details['experience']} years of leadership experience in {details['qualification']}, I have consistently "
                                f"delivered exceptional results and led high-performing teams. My achievements include {details['achievements']}. "
                                f"I am known for my strategic vision and my ability to drive change. My leadership style is characterized by my ability "
                                f"to inspire and motivate others to achieve their best. I am committed to professional excellence and always strive to exceed expectations.",
            "work_history": generate_work_history(details['locations'], details['roles'], details['achievements']),
            "contact": f"Contact Information:\nEmail: {details['email']}\nPhone: {details['phone']}\nAddress: {details['address']}",
            "skills": f"Key Skills: {', '.join(details['skills'])}",
            "education": generate_education(details['schools'], details['years'], details['degrees']),
            "personal_info": f"Name: {details['name']}\nAge: {details['age']}\nGender: {details['gender']}"
        },
        "Template 9: ": {
            "professional_exp": f"Dynamic professional with {details['experience']} years of experience in {details['qualification']}. Notable achievements: {details['achievements']}. "
                                f"My career has been marked by my ability to excel in challenging environments and deliver exceptional results. I am committed to continuous learning and professional growth. "
                                f"My ability to adapt to new challenges and continuously improve my skill set has been key to my success.",
            "work_history": generate_work_history(details['locations'], details['roles'], details['achievements']),
            "contact": f"Contact:\nEmail: {details['email']}\nPhone: {details['phone']}\nAddress: {details['address']}",
            "skills": f"Competencies: {', '.join(details['skills'])}",
            "education": generate_education(details['schools'], details['years'], details['degrees']),
            "personal_info": f"Name: {details['name']}\nAge: {details['age']}\nGender: {details['gender']}"
        },

        "Template 10: ": {
            "professional_exp": f"Experienced in {details['qualification']} for {details['experience']} years. Key achievements include {details['achievements']}. "
                                f"My career has been defined by my ability to deliver results and drive change. I am committed to professional excellence and always strive to exceed expectations. "
                                f"My focus is on achieving the best possible outcomes and making a positive impact.",
            "work_history": generate_work_history(details['locations'], details['roles'], details['achievements']),
            "contact": f"Reach Out:\nEmail: {details['email']}\nPhone: {details['phone']}\nLocation: {details['address']}",
            "skills": f"Proficiencies: {', '.join(details['skills'])}",
            "education": generate_education(details['schools'], details['years'], details['degrees']),
            "personal_info": f"Name: {details['name']}\nAge: {details['age']}\nGender: {details['gender']}"
        },
    }

    selected_template = random.choice(list(templates.keys()))

    resume = "\n\n".join([templates[selected_template][section] for section in templates[selected_template]])

    return resume

