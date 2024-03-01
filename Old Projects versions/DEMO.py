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
def replace_tokens(template_file, output_file, replacements):
    with open(template_file, 'r') as f:
        template = f.read()

    for placeholder, value in replacements.items():
        if isinstance(value, list):
            value = ', '.join(map(str, value))
        template = template.replace(placeholder, str(value))

    with open(output_file, 'w') as f:
        f.write(template)
    print(output_file)

def PDFlatex(latex_file):
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
    #option = st.radio(label = "What format do you want your résumé in?", options = ["Word", "PDF"])
    submitted = st.form_submit_button("Submit")
    patience = st.empty()

wait = st.empty() 

# All GPT functions create separate things, ex. introGPT polishes the resume, workGPT orders and makes the work details sound better,
# skill just arranges the skills, proj changes up the project description to sound better, and cert just puts in the certification
def introGPT():
    prompt = intro + '. change this to sound better for a resume, make it a 2-3 sentences. Dont add any quotes around it and no period should be at the beginning. The symbol "-" is not allowed anywhere'
    model = "gpt-3.5-turbo-instruct"
    response = openai.Completion.create(model=model, prompt=prompt, max_tokens = 700)
    global ans
    ans = response.choices[0].text
    if intro == '':
        ans = ''
def workGPT():
    starterPrompt = r'. change this to sound better for a resume, make sure that each job has their own bullet points. after each bullet point make a new line, add no quotes. Also, this will be going into latex code, so make sure to format it correctly. If theres a % symbol, make sure that its \% instead of %. DO NOT PUT A PERIOD AT THE BEGINNING'
    if rTemplates == img1:
        prompt = workedAt + starterPrompt + '. change this to sound better for a resume. The latex format should be "\textbf{Job title -- Company, City, Country -- Years Active}". The info about the job should be itemized. DO NOT USE TEXTIT'
    elif rTemplates == img2:
        prompt = workedAt + starterPrompt + r'The title format should be something like this: \textbf{JOB \hfill City, Country} \\  \textit{COMPANY, YEARS}. DONT CHANGE THE FORMAT.'
    elif rTemplates == img3:
        prompt = workedAt + starterPrompt + r'The title should be in this format: textbf{title} textit{place} place (if applicable) then \hfill year. the place shouldnt be in \textit'
        #make the response in one line. additionally, make sure \being{itemize} sticks with \textbf{} and \textbf{} sticks with \end{itemize}
    model = "gpt-3.5-turbo-0613"
    response = openai.ChatCompletion.create(model=model,messages=[{"role": "system", "content": "You are a helpful assistant."},
                                                                  {"role": "user", "content": prompt}], max_tokens=700)
    global ans1
    ans1 = response['choices'][0]['message']['content']
    if workedAt == '':
        ans1 = ''
    lines = ans1.split('\n')
    ans1 = '\n'.join(line for line in lines if line.strip())
def skillGPT():
    prompt = skillsIn + '. just list them using commas. Make sure everything is on one line, no extra spaces except after a comma.'
    model = "gpt-3.5-turbo-0613"
    response = openai.ChatCompletion.create(model=model,messages=[{"role": "system", "content": "You are a helpful assistant."},
                                                                  {"role": "user", "content": prompt}], max_tokens=700)
    global ans2
    ans2 = response['choices'][0]['message']['content']
    if skillsIn == '':
        ans2 = ''
def projGPT():
    prompt = projectsDone + r'. make this to sound better, this is for a resume. Make sure the project title format is \textbf{proj name} and that the project info is in \begin{itemize} as \item NO DASHES ALLOWED . DO NOT PUT A PERIOD IN THE BEGINNING. do not duplicate projects'
    if rTemplates == img2:
        prompt = prompt + 'Make sure there are no blank lines in the response and nothing should be bolded. everything should be regular font. No dashes allowed'
    if rTemplates == img3:
        prompt = prompt + 'Make sure that the format is \textbf{project name}, \texit{company} (if one is given), and place (if one is given) DO NOT PUT TWO \\ AFTER TEXTBF, IT SHOULD ONLY BE 1 \.'
    model = "gpt-3.5-turbo-0613"
    response = openai.ChatCompletion.create(model=model,messages=[{"role": "system", "content": "You are a helpful assistant."},
                                                                  {"role": "user", "content": prompt}], max_tokens=700)
    global ans3
    ans3 = response['choices'][0]['message']['content']
    if projectsDone == '':
        ans3 = ''
    plines = ans3.split('\n')
    ans3 = '\n'.join(line for line in plines if line.strip())
def certGPT():
    prompt = certsObtain + '. reformat this for a resume, dont put any quotes in. Whatever the user inputs should be formatted, dont add anything else in.'
    model = "gpt-3.5-turbo-0613"
    response = openai.ChatCompletion.create(model=model,messages=[{"role": "system", "content": "You are a helpful assistant."},
                                                                  {"role": "user", "content": prompt}], max_tokens=700)
    global ans4
    ans4 = response['choices'][0]['message']['content']
    if certsObtain == '':
        ans4 = ''
def eduGPT():
    prompt = educationPlace + r'. change this to sound better, this is for a resume. The format should be \textbf{degree}\\{school name and place -- Graduated: year}. DO NOT ALTER THE FORMAT. DONT DELETE DUPLICATES'
    if rTemplates == img2:
        prompt = educationPlace + r'. change this to sound better, this is for a resume. Put your response in this format:\textbf{University of XYZ \hfill City, Country}\\ \textit{DEGREE NAME, YEARS}}. IF YEARS ISNT PROVIDED DONT ADD IT IN. DONT ADD DUPLICATES. Make sure that there are no parentheses around the year.'
    elif rTemplates == img3:
        prompt = educationPlace + r'. change this to sound better, this is for a resume. The format should be year \textbf{degree} \textit{school name}, place (if applicable). DO NOT ALTER THE FORMAT. DONT DELETE DUPLICATES. Make sure that there are no parentheses around the year'
    model = "gpt-3.5-turbo-0613"
    response = openai.ChatCompletion.create(model=model,messages=[{"role": "system", "content": "You are a helpful assistant."},
                                                                  {"role": "user", "content": prompt}], max_tokens=700)
    global ans5
    ans5 = response['choices'][0]['message']['content']
    # if educationPlace == '':
    #     ans5 = ''

global rebuild 
rebuild = 0
# Function starts combines all of the previous GPT functions
def startGPT():
    try:
        introGPT()
        workGPT()
        time.sleep(30)
        skillGPT()
        projGPT()
        time.sleep(25)
        certGPT()
        eduGPT()
        global resume_data
        resume_data = {
            'fname': fname,
            'lname': lname,
            'eAdd': eAdd,
            'phones': phones,
            'linkedinSite': linkedinSite,
            'educationPlace': educationPlace,
            'intro': ans,
            'workedAt': ans1,
            'skillsIn': ans2,
            'projectsDone': ans3,
            'certsObtain': ans4,
            'educationPlace': ans5
        }
    except openai.error.RateLimitError as e:
      retry_time = e.retry_after if hasattr(e, 'retry_after') else 35
      wait.error(f"You have used the Résumé Builder multiple times, please wait for {retry_time} seconds.")
      time.sleep(retry_time)
      wait.write("Rebuilding Résumé...")
      time.sleep(2)
      wait.empty()
      startGPT()
      rebuild += 1

# If statements below choose the PDF template that was selected and creates the resume
if submitted == True and rTemplates == img1:
    time.sleep(1)
    patience.write("Conversion to PDF requires some time. We appreciate your patience.")
    eAdd = eAdd.replace("_", r"\_")
    linkedinSite = linkedinSite.replace("_", r"\_")
    
    startGPT()
    st.write(rebuild)
    replace_tokens(temp1, resume1, resume_data)
    PDFlatex(resume1)
    if rebuild >= 1:
        st.write("Rebuilt Résumé")
    patience.empty()
elif submitted == True and rTemplates == img2:
    time.sleep(1)
    patience.write("Conversion to PDF requires some time. We appreciate your patience.")
    eAdd = eAdd.replace("_", r"\_")
    linkedinSite = linkedinSite.replace("_", r"\_")
    
    startGPT()
    replace_tokens(temp2, resume2, resume_data)
    PDFlatex(resume2)
        
    patience.empty()
elif submitted == True and rTemplates == img3:
    time.sleep(1)
    patience.write("Conversion to PDF requires some time. We appreciate your patience.")
    eAdd = eAdd.replace("_", r"\_")
    linkedinSite = linkedinSite.replace("_", r"\_")
    
    startGPT()
    replace_tokens(temp3, resume3, resume_data)
    PDFlatex(resume3)
        
    patience.empty()