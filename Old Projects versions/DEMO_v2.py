from config import *
#from GPT import *
#from conversions import *
from streamlit_image_select import image_select
from pdf2image import convert_from_path
import streamlit as st
import openai
import time
openai.api_key = api_key

st.title('Welcome to the Résumé Builder!')
tPaths = [t1, t2, t3]
x = 0

import subprocess
# Replace tokens + pdflatex can be moved to a different file, however an error form occurs.
def tokens_latex(template_file, latex_file, replacements):
    with open(template_file, 'r') as f:
        template = f.read()

    for placeholder, value in replacements.items():
        if isinstance(value, list):
            value = ', '.join(map(str, value))
        template = template.replace(placeholder, str(value))

    with open(latex_file, 'w') as f:
        f.write(template)
    subprocess.run([PDFpath, '--interaction=nonstopmode', latex_file], check=True)
    subprocess.run([PDFpath, '--interaction=nonstopmode','-output-directory', '.', latex_file], check=True)

def display_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    for i, image in enumerate(images):
        st.image(image, use_column_width=True)

st.text("Please Enter in your Information")
with st.form("InformationForm"):
    rTemplates = image_select("Please Choose a Template", [img1, img2, img3]) #img1, img2, img3 are pics of the templates in dropbox
    for path in tPaths: #Loop is for the template naming scheme
        if x == 0:
            title = "Template 1"
        elif x == 1:
            title = "Template 2"
        else:
            title = "Template 3"
        with st.expander(f"View {title}"):
            display_pdf(path)
        x += 1
    
    #The following is putting a title with a default description in the second parameter
    fname = st.text_area("First Name*", "John")
    lname = st.text_area("Last Name*", "Doe")
    eAdd = st.text_area("Email*", "jd@gmail.com")
    phones = st.text_area("Phone Number*", "123-456-7890")
    linkedinSite = st.text_area("LinkedIn URL*", "linkedin.com/in/johndoe")
    intro = st.text_area("Professional Summary*", "Versatile and results-driven software engineer with expertise in full-stack web development, specializing in Python and Django. Proven track record of delivering high-impact projects and collaborating effectively within cross-functional teams. Dedicated to designing scalable solutions and passionate about solving complex problems.")
    educationPlace = st.text_area("Education*", "2015 - 2019 Bachelor of Science in Computer Science, University of XYZ, City, Country")
    workedAt = st.text_area("Work Experience*", """2019-Present Software Engineer, Tech Solutions Inc., City, Country
Developed and maintained web applications using Python, Django, and JavaScript, delivering feature-rich and responsive
user interfaces.
Led the implementation of a modular and scalable e-commerce platform, resulting in a 20%
Conducted code reviews, provided mentorship to junior developers, and actively participated in continuous improvement
initiatives.
2017-2019 Intern, Software Development, ABC Tech, City, Country
Contributed to the design and development of new software features, demonstrating proficiency in Java, JavaScript, and
SQL.
Assisted in the implementation of a data analytics tool, enabling the team to gain valuable insights into user behavior.
2016 - 2017 IT Support Specialist, XYZ Company, City, Country
Provided technical support to end-users, diagnosing and resolving hardware and software issues in a timely manner.
Implemented system upgrades and maintenance procedures, ensuring optimal performance of computer systems.""")
    skillsIn = st.text_area("Skills*", "Python, C++, JavaScript, Django, MySQL, PostgreSQL, AWS, Git, Docker, Jenkins, Puppet, Chef, Terraform")
    projectsDone = st.text_area("Projects*", """E-commerce Platform, Tech Solutions Inc., City, Country
Led the development of a scalable and modular e-commerce platform using Python, Django, and React.
Implemented secure payment gateways, product recommendation algorithms, and enhanced user authentication mechanisms.""")
    certsObtain = st.text_area("Certifications and Training*", "Certified Python Developer (XYZ Certification)")
    submitted = st.form_submit_button("Submit")
    patience = st.empty()

wait = st.empty()
eAdd = eAdd.replace("_", r"\_")
linkedinSite = linkedinSite.replace("_", r"\_")
pdfname = fname.capitalize() + ' ' + lname.capitalize() +"'s Résumé.tex"
resume_data = {
            'fname': fname,
            'lname': lname,
            'eAdd': eAdd,
            'phones': phones,
            'linkedinSite': linkedinSite
}

vdict = ["intro", "skillsIn", "certsObtain", "workedAt", "projectsDone", "educationPlace"]
workPrompt = r'. change this to sound better for a resume, make sure that each job has their own bullet points. after each bullet point make a new line, add no quotes. Also, this will be going into latex code, so make sure to format it correctly. If theres a % symbol, make sure that its \% instead of %. DO NOT PUT A PERIOD AT THE BEGINNING'
projPrompt = '. make this to sound better, this is for a resume.'
prmpt_dict = {"intro":". change this to sound better for a resume, make it a 2-3 sentences. Dont add any quotes around it and no period should be at the beginning. The symbol '-' is not allowed anywhere",
              "skillsIn":". list them using commas. Everything has to be on one line.",
              "certsObtain":". reformat this for a resume, dont put any quotes in. Whatever the user inputs should be formatted, dont add anything else in.",
              "workedAt1":workPrompt + "change this to sound better for a résumé. The latex format: '\textbf{Job title -- Company, City, Country -- Years Active}'. The info about the job should be itemized. DO NOT USE TEXTIT",
              "workedAt2":workPrompt + r'format: \textbf{JOB \hfill City, Country} \\  \textit{COMPANY, YEARS}. DONT CHANGE THE FORMAT.',
              "workedAt3":workPrompt + r'format: textbf{title} textit{place} place (if applicable) then \hfill year. the place shouldnt be in \textit',
              "projectsDone1":projPrompt + r'format: \textbf{proj name} and that the project info is in \begin{itemize} as \item, NO "-" . DO NOT PUT A PERIOD IN THE BEGINNING. do not duplicate projects. do not start with certifications:',
              "projectsDone2":projPrompt + "no blank lines should be in the response and everything should be regular font. No dashes allowed.",
              "projectsDone3":projPrompt + "format: \textbf{project name}, \texit{company} (if one is given), and place (if one is given) DO NOT PUT TWO \\ AFTER TEXTIT, IT SHOULD ONLY BE 1 \.",
              "educationPlace1":r'format should be \textbf{degree}\\{school name and place -- Graduated: year}. DO NOT ALTER THE FORMAT. DONT DELETE DUPLICATES. if theres more than one education, put a \\ at the end of each one',
              "educationPlace2":r'format should be:\textbf{University of XYZ \hfill City, Country}\\ \textit{DEGREE NAME, YEARS}}. IF YEARS ISNT PROVIDED DONT ADD IT IN. NO DUPLICATES, MAKE SURE EACH ONE IS STILL INCLUDED. No parentheses around the year. if theres more than one education, put a \\ at the end of each one. MAKE SURE THERE ARE NO BLANK LINES AFTER EACH EDUCATION i.e. after year there should be a\\ and below should be the next education if there is one',
              "educationPlace3":r'format: year \textbf{degree} \textit{school name}, place (if applicable). DO NOT ALTER THE FORMAT. DONT DELETE DUPLICATES. No parentheses around the year. if theres more than one education, put a \\ at the end of each one'
              }

def callGPT(stVar, prmpt, nums):
    prompt = stVar + prmpt
    model = "gpt-3.5-turbo-0613"
    response = openai.ChatCompletion.create(model=model,messages=[{"role": "system", "content": "You are a helpful assistant."},
                                                                  {"role": "user", "content": prompt}], max_tokens=500)
    ans = response['choices'][0]['message']['content']
    if stVar == workedAt or stVar == projectsDone:
        lines = ans.split('\n')
        ans = '\n'.join(line for line in lines if line.strip())
    ans = ans.replace("&", r"\&").replace("$", r"\$").replace("%", r"\%").replace("#", r"\#").replace("_", r"\_").replace("\+\+", "++")
    resume_data[vdict[nums]] = ans

# global variable for rate limit error
global rebuild
rebuild = 0

# Function starts combines all of the previous GPT functions
def startGPT():
    counter = 0
    #try:
    callGPT(intro, prmpt_dict["intro"], counter)
    counter += 1
    callGPT(skillsIn, prmpt_dict["skillsIn"], counter)
    counter += 1
    time.sleep(30)
    callGPT(certsObtain, prmpt_dict["certsObtain"], counter)
    counter += 1
    if rTemplates == img1:
        callGPT(workedAt, prmpt_dict["workedAt1"], counter)
        counter += 1
        time.sleep(25)
        callGPT(projectsDone, prmpt_dict["projectsDone1"], counter)
        counter += 1
        callGPT(educationPlace, prmpt_dict["educationPlace1"], counter)
    elif rTemplates == img2:
        callGPT(workedAt, prmpt_dict["workedAt2"], counter)
        counter += 1
        time.sleep(25)
        callGPT(projectsDone, prmpt_dict["projectsDone2"], counter)
        counter += 1
        callGPT(educationPlace, prmpt_dict["educationPlace2"], counter)
    elif rTemplates == img3:
        callGPT(workedAt, prmpt_dict["workedAt3"], counter)
        counter += 1
        time.sleep(25)
        callGPT(projectsDone, prmpt_dict["projectsDone3"], counter)
        counter += 1
        callGPT(educationPlace, prmpt_dict["educationPlace3"], counter)
    time.sleep(30)
    # except openai.error.RateLimitError as e:
    #     retry_time = e.retry_after if hasattr(e, 'retry_after') else 35
    #     #wait.error(f"You have used the Résumé Builder multiple times, please wait for {retry_time} seconds.")
    #     time.sleep(retry_time)
    #     wait.write("Rebuilding Résumé...")
    #     time.sleep(2)
    #     wait.empty()
    #     startGPT()
    #     global rebuild
    #     rebuild += 1

if submitted == True and rTemplates == img1:
    time.sleep(1)
    patience.write("Conversion to PDF requires some time. We appreciate your patience.")
    startGPT()
    tokens_latex(temp1, pdfname, resume_data)
    if rebuild >= 1:
        st.write("Rebuilt Résumé")
    patience.write("Résumé has been built.")
    patience.empty()
    rebuild = 0
elif submitted == True and rTemplates == img2:
    time.sleep(1)
    patience.write("Conversion to PDF requires some time. We appreciate your patience.")
    startGPT()
    tokens_latex(temp2, pdfname, resume_data)
    patience.empty()
    rebuild = 0
elif submitted == True and rTemplates == img3:
    time.sleep(1)
    patience.write("Conversion to PDF requires some time. We appreciate your patience.")
    startGPT()
    tokens_latex(temp3, pdfname, resume_data)
    patience.empty()
    rebuild = 0
