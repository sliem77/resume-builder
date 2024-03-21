from imgs import *
from streamlit_image_select import image_select
from pdf2image import convert_from_path
from pdf2docx import Converter
from dotenv import load_dotenv
import streamlit as st
import openai
import subprocess
import time
import subprocess
import os
import shutil
from PyPDF2 import PdfReader
from docx import Document
import json
openai.api_key = os.environ.get('OPENAI_API_KEY')

load_dotenv()

st.title('Welcome to the Résumé Builder!')
tPaths = [t1, t2, t3]
x = 0
first_dict = {
    'fname': "",
    'lname': "" ,
    'eAdd': "" ,
    'phones': "" ,
    'linkedinSite': "" ,
    'educationPlace': "" ,
    'intro': "" ,
    'workedAt': "" ,
    'skillsIn': "" ,
    'projectsDone': "" ,
    'certsObtain': "" ,
    'educationPlace': "" 
}

form_info = {}
# Replace tokens + pdflatex can be moved to a different file, however an error form occurs.
def tokens_latex(template_file, latex_file, replacements):
    with open(template_file, 'r') as f:
        template = f.read()

    for placeholder, value in replacements.items():
        if isinstance(value, list):
            value = ', '.join(map(str, value))
        template = template.replace(placeholder, str(value))
    
    file_path = os.path.join("/tmp", latex_file.lstrip('/'))
    with open(file_path, 'w') as f:
        f.write(template)
    
    outputdir = '/tmp/output/'
    os.makedirs(outputdir, exist_ok=True)
    shutil.copy2(file_path, outputdir)
    
    ltxoutput = os.path.join(outputdir, os.path.basename(latex_file))
    subprocess.run(['pdflatex', '--interaction=nonstopmode', '-output-directory', outputdir, ltxoutput], check=True, capture_output=True)
    
    with open(ltxoutput, 'rb') as file:
        doc_content = file.read()
    
    pdf_path = os.path.splitext(ltxoutput)[0] + '.pdf'
    with open(pdf_path, 'rb') as pdf_file:
        pdf_content = pdf_file.read()
    
    if option == "PDF":
        st.download_button(label="Download PDF ", data=pdf_content, file_name=os.path.basename(pdf_path))
    elif option == "Word":
        docx = os.path.join(outputdir, docname)
        cv = Converter(pdf_path)
        cv.convert(docx, start=0, end=None)
        cv.close()
        with open(docx, 'rb') as docx_file:
            doc_content = docx_file.read()
        st.download_button(label="Download Word", data=doc_content, file_name=os.path.basename(docx))

def display_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    for i, image in enumerate(images):
        st.image(image, use_column_width=True)

def pdfText(pdf):
    text = ""
    with open(pdf, "rb") as file:
        pdf_reader = PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def docText(docs):
    text = ""
    doc = Document(docs)
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

st.text("Please Enter in your Information")
uploaded_file = st.file_uploader("Have an existing Résumé? Drop your Résumé here to autofill the form!", type=("PDF", "DOCX", "DOC", "TXT")) #txt is only temporary

def fillGPT(info, dict1):
    prompt = info + ": This is  my resume, when you put those values in this dictionary, make sure there are no quotes, double quotes, brackets, or parentheses, it should be all text only. DO NOT ELIMINATE ANY BULLET POINTS. Make sure to differentiate between projects and work experience. No nested key values or nested dictionaries, if one is needed, make sure that the info from that is inside the value, no nested values should be given. You don't need to format it, because it will be fixed later on. Usually, there should be a projects section which is listed like this 'PROJECTS:', sometimes there's not, its ok to keep it empty sometimes, so if theres no section there, then put nothing. List the skills using commas. DO NOT DELETE THE WORK INFO IN THE WORK SECTION, IT IS VERY IMPORTANT. Work is usually shown as 'Work: ' or 'Work Experince: '. STOP CONFUSING WORK FOR PROJECTS, PROJECTS ARE ALWAYS UNDER A PROJECT SECTION! STOP GETTING RID OF THE WORK EXPERIENCE. WORK EXPERINCE IS IN ITS OWN SECTION. When doing this, think a little bit more and wonder how would this dictionary look in a fill out form where each dict key is the form fill out value.  Here's the dictionary: " + str(dict1)
    model = "gpt-3.5-turbo-1106"
    response = openai.ChatCompletion.create(model=model,messages=[{"role": "system", "content": "You are a helpful assistant. Generate a dictionary from the given resume. Preserve all work experience details and avoid eliminating any bullet points. When that is completed, put that work experience inside workedAt, not projectsDone."},
                                                                  {"role": "user", "content": prompt + "json"},
                                                                  {"role": "user", "content": "Create a dictionary with the values."}], 
                                            max_tokens=1500, temperature=0.1, response_format = { "type": "json_object" })
    ans = response['choices'][0]['message']['content']
    fixedInfo = ans.replace('\\n', '')
    formInfo = json.loads(fixedInfo)
    return formInfo

if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        with open("resume.pdf", "wb") as pdf:
            pdf.write(uploaded_file.getvalue())
            pdf_text = pdfText("resume.pdf")
            form_info = fillGPT(pdf_text, first_dict)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        with open("resume.docx", "wb") as doc:
            doc.write(uploaded_file.getvalue())
            doc_text = docText("resume.docx")
            form_info = fillGPT(doc_text, first_dict)
            
default_fname = form_info.get('fname')
default_lname = form_info.get('lname')
default_eAdd = form_info.get('eAdd')
default_phones = form_info.get('phones')
default_linkedinSite = form_info.get('linkedinSite')
default_intro = form_info.get('intro')
default_educationPlace = form_info.get('educationPlace')
default_workedAt = form_info.get('workedAt')
default_skillsIn = form_info.get('skillsIn')
default_projectsDone = form_info.get('projectsDone')
default_certsObtain = form_info.get('certsObtain')

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
    fname = st.text_area("First Name*", default_fname)
    lname = st.text_area("Last Name*", default_lname)
    eAdd = st.text_area("Email*", default_eAdd)
    phones = st.text_area("Phone Number*", default_phones)
    linkedinSite = st.text_area("LinkedIn URL*", default_linkedinSite)
    intro = st.text_area("Professional Summary*", default_intro)
    educationPlace = st.text_area("Education*", default_educationPlace)
    workedAt = st.text_area("Work Experience*", default_workedAt)
    skillsIn = st.text_area("Skills*", default_skillsIn)
    projectsDone = st.text_area("Projects*", default_projectsDone)
    certsObtain = st.text_area("Certifications and Training*", default_certsObtain)
    option = st.radio(label = "What format do you want your résumé in?", options = ["PDF", "Word"])
    submitted = st.form_submit_button("Submit")
    patience = st.empty()

wait = st.empty()
resume_data = {
            'fname': fname,
            'lname': lname,
            'eAdd': eAdd,
            'phones': phones,
            'linkedinSite': linkedinSite
}

vdict = ["intro", "skillsIn", "certsObtain", "workedAt", "projectsDone", "educationPlace"]
workPrompt = r'. change this to sound better for a resume, make sure that each job has their own bullet points. after each bullet point make a new line, add no quotes. Also, this will be going into latex code, so make sure to format it correctly. If theres a % symbol, make sure that its \% instead of %. DO NOT PUT A PERIOD AT THE BEGINNING.'
workFix = r'. Also, when doing \begin{itemize} dont forget to end it with \end{itemize}'
projPrompt = '. make this to sound better, this is for a resume.'
prmpt_dict = {"intro":". change this to sound better for a resume, make it a 2-3 sentences. Dont add any quotes around it and no period should be at the beginning. The symbol '-' is not allowed anywhere",
              "skillsIn":". JUST GIVE SKILLS ONLY, separated by commas, no '-' allowed. I dont want your custom response, just the skills only.",
              "certsObtain":". reformat this for a resume, dont put any quotes in. Whatever the user inputs should be formatted, dont add anything else in. Certification name only. Do not Put certification:, just list the name only",
              "workedAt1":workPrompt + "change this to sound better for a résumé. The latex format: '\textbf{Job title -- Company, City, Country -- Years Active}'. The info about the job should be itemized. DO NOT USE TEXTIT. MAKE SURE THE YEAR IS SHOWN." + workFix,
              "workedAt2":workPrompt + r'format: \textbf{JOB \hfill City, Country} \\  \textit{COMPANY, YEARS}. DONT CHANGE THE FORMAT. MAKE SURE THE YEAR IS SHOWN' + workFix,
              "workedAt3":workPrompt + r'format: textbf{title} textit{place} place (if applicable) then \hfill year. the place shouldnt be in \textit MAKE SURE THE YEAR IS SHOWN. Also, make sure that each work experience is 3-4 bullet points. Do not add anything random.' + workFix,
              "projectsDone1":projPrompt + r'format: \textbf{proj name} and that the project info is in \begin{itemize} as \item, NO "-" . DO NOT PUT A PERIOD IN THE BEGINNING. do not duplicate projects. do not start with certifications:',
              "projectsDone2":projPrompt + "no blank lines should be in the response and everything should be regular font. No dashes allowed.",
              "projectsDone3":projPrompt + "format: \textbf{project name}, \texit{company} (if one is given), and place (if one is given) DO NOT PUT TWO \\ AFTER TEXTIT, IT SHOULD ONLY BE 1 \.",
              "educationPlace1":r'format should be \textbf{degree}\\{school name and place -- Graduated: year}. DO NOT ALTER THE FORMAT. DONT DELETE DUPLICATES. if theres more than one education, put a \\ at the end of each one',
              "educationPlace2":r'format should be:\textbf{University of XYZ \hfill City, Country}\\ \textit{DEGREE NAME, YEARS}} (if applicable). IF YEARS ISNT PROVIDED DONT ADD IT IN. NO DUPLICATES, MAKE SURE EACH ONE IS STILL INCLUDED. No parentheses around the year. if theres more than one education, put a \\ at the end of each one. MAKE SURE THERE ARE NO BLANK LINES AFTER EACH EDUCATION i.e. after year there should be a\\ and below should be the next education if there is one. If there isnt then there should be no \\.',
              "educationPlace3":r'format: year \textbf{degree} \textit{school name}, place (if applicable). DO NOT ALTER THE FORMAT. DONT DELETE or CREATE DUPLICATES. No parentheses around the year. if theres more than one education, put a \\ at the end of each one.'
              }

def callGPT(stVar, prmpt, nums):
    if stVar == "" or stVar is None:
        resume_data[vdict[nums]] = ""
        return
    if stVar == skillsIn and rTemplates == img1:
        prmpt = "itemize the skills, it should be in one item only, no '-' allowed. I dont want your custom response, just the skills only."
    prompt = stVar + prmpt
    model = "gpt-3.5-turbo-0613"
    response = openai.ChatCompletion.create(model=model,messages=[{"role": "system", "content": "You are a helpful assistant."},
                                                                  {"role": "user", "content": prompt}], max_tokens=900)
    ans = response['choices'][0]['message']['content']
    if stVar == workedAt or stVar == projectsDone:
        lines = ans.split('\n')
        ans = '\n'.join(line for line in lines if line.strip())
    ltxspecials = ['&', '$', '%', '#', '_', '++']
    ltxmodified = [r'\&', r'\$', r'\%', r'\#', r'\_', '++']

    for char1, char2 in zip(ltxspecials, ltxmodified):
        if '\\' + char1 in ans:
            continue
        ans = ans.replace(char1, char2)
    resume_data[vdict[nums]] = ans

# global variable for rate limit error
global rebuild
rebuild = 0

# Function starts combines all of the previous GPT functions
def startGPT():
    counter = 0
    try:
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
    except openai.error.RateLimitError as e:
        retry_time = e.retry_after if hasattr(e, 'retry_after') else 35
        wait.error(f"The Résumé Builder has been used multiple times, please wait for {retry_time} seconds.")
        time.sleep(retry_time)
        wait.write("Rebuilding Résumé...")
        time.sleep(2)
        wait.empty()
        startGPT()
        global rebuild
        rebuild += 1
    except subprocess.CalledProcessError as s:
        wait.error(f"The Résumé Builder has encountered an error.")
        wait.write("Rebuilding Résumé...")
        time.sleep(2)
        wait.empty()
        startGPT()

if submitted == True and rTemplates == img1:
    time.sleep(1)
    patience.write("Conversion to PDF requires some time. We appreciate your patience.")
    eAdd = eAdd.replace("_", r"\_")
    linkedinSite = linkedinSite.replace("_", r"\_")
    pdfname = fname.capitalize() + ' ' + lname.capitalize() +" Résumé.tex"
    docname = fname.capitalize() + ' ' + lname.capitalize() +" Résumé.docx"
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
    eAdd = eAdd.replace("_", r"\_")
    linkedinSite = linkedinSite.replace("_", r"\_")
    pdfname = fname.capitalize() + ' ' + lname.capitalize() +" Résumé.tex"
    docname = fname.capitalize() + ' ' + lname.capitalize() +" Résumé.docx"
    startGPT()
    tokens_latex(temp2, pdfname, resume_data)
    if rebuild >= 1:
        st.write("Rebuilt Résumé")
    patience.write("Résumé has been built.")
    patience.empty()
    rebuild = 0
elif submitted == True and rTemplates == img3:
    time.sleep(1)
    patience.write("Conversion to PDF requires some time. We appreciate your patience.")
    eAdd = eAdd.replace("_", r"\_")
    linkedinSite = linkedinSite.replace("_", r"\_")
    pdfname = fname.capitalize() + ' ' + lname.capitalize() +" Résumé.tex"
    docname = fname.capitalize() + ' ' + lname.capitalize() +" Résumé.docx"
    startGPT()
    tokens_latex(temp3, pdfname, resume_data)
    if rebuild >= 1:
        st.write("Rebuilt Résumé")
    patience.write("Résumé has been built.")
    patience.empty()
    rebuild = 0
