#pip install streamlit
#pip install openai
#pip install flask
#importing all necessary packages
from config import api_key, PDFpath, DOCpath
import streamlit as st
import openai
import subprocess
openai.api_key = api_key

st.title('Welcome to the Résumé Builder!')
st.text("Please Enter in your Information")

#Form creation to gain info for résumé
with st.form("Information"):
    fname = st.text_input("First Name")
    lname = st.text_input("Last Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    linkedin = st.text_input("LinkedIn URL")
    intro = st.text_input("Professional Summary")
    education = st.text_input("Education")
    work = st.text_input("Work Experience")
    skills = st.text_input("Skills")
    projects = st.text_input("Projects")
    certs = st.text_input("Certifications")
    option = st.radio(label = "What format do you want your résumé in?", options = ["Word", "PDF"])
    submitted = st.form_submit_button("Submit")

## The following code in comments is a template that would be used to create the user's résumé:
    # template = r"""
    # \documentclass[a4paper,10pt]{article}
    # \usepackage[left=1in, right=1in, top=1in, bottom=1in]{geometry}
    # \usepackage{enumitem}
    # \usepackage{parskip}
    # \usepackage{titlesec}

    # \titleformat{\section}{\large\bfseries}{\thesection}{1em}{}[{\titlerule[0.8pt]}]

    # \begin{document}

    # \pagestyle{empty}

    # \begin{center}
    #     \textbf{\LARGE John Doe} \\
    #     123 Main Street, Cityville, State ZIP Code | (555) 555-5555 | john.doe@email.com | LinkedIn: linkedin.com/in/johndoe
    # \end{center}

    # \section*{Objective}
    # Experienced and results-driven Mechanical Engineer with a decade of expertise in designing and implementing innovative solutions. Proven track record of success in project management, team leadership, and delivering high-quality engineering solutions. Seeking a challenging role to contribute technical acumen and managerial skills.

    # \section*{Professional Experience}

    # \textbf{Senior Mechanical Engineer | XYZ Engineering Solutions, Cityville, USA | 2018-2022}
    # \begin{itemize}[left=0.5in]
    #     \item Led a team of 10 engineers in designing and executing projects, resulting in a 20\% increase in overall project efficiency.
    #     \item Developed and implemented cost-effective design modifications, reducing production costs by 15\%.
    #     \item Conducted feasibility studies and collaborated with cross-functional teams to ensure project success.
    # \end{itemize}

    # \textbf{Mechanical Design Engineer | ABC Manufacturing, Townsville, USA | 2015-2018}
    # \begin{itemize}[left=0.5in]
    #     \item Spearheaded the design and development of a new product line, increasing company revenue by 25\%.
    #     \item Implemented Lean Manufacturing principles, resulting in a 30\% reduction in production cycle time.
    #     \item Collaborated with suppliers to source cost-effective materials, reducing project costs by 10\%.
    # \end{itemize}

    # \textbf{Project Engineer | DEF Technology Innovations, Riverside, USA | 2012-2015}
    # \begin{itemize}[left=0.5in]
    #     \item Managed the entire project lifecycle, from conception to delivery, ensuring adherence to timelines and budgets.
    #     \item Conducted thorough risk assessments and implemented mitigation strategies, resulting in a 15\% reduction in project delays.
    #     \item Provided technical expertise and support to cross-functional teams, fostering collaboration and innovation.
    # \end{itemize}

    # \textbf{Junior Mechanical Engineer | GHI Engineering Services, Cityville, USA | 2010-2012}
    # \begin{itemize}[left=0.5in]
    #     \item Assisted in the design and testing of mechanical components for various projects.
    #     \item Conducted detailed analysis and troubleshooting, contributing to the resolution of complex technical issues.
    #     \item Collaborated with senior engineers to streamline design processes and improve overall project efficiency.
    # \end{itemize}

    # \section*{Skills}
    # \begin{flushleft}
    # \textbf{Technical Skills:}
    # \begin{itemize}[left=0.5in]
    #     \item SolidWorks, AutoCAD, and other CAD software proficiency
    #     \item Finite Element Analysis (FEA)
    #     \item Prototyping and testing
    # \end{itemize}

    # \textbf{Soft Skills:}
    # \begin{itemize}[left=0.5in]
    #     \item Project management and leadership
    #     \item Strong problem-solving skills
    #     \item Excellent communication and interpersonal abilities
    # \end{itemize}
    # \end{flushleft}

    # \section*{Education}
    # \textbf{Bachelor of Science in Mechanical Engineering} \\
    # University of Engineering, Cityville, USA | Graduated: 2010

    # \section*{Certifications}
    # \begin{itemize}[left=0.5in]
    #     \item Professional Engineer (PE) License
    #     \item Project Management Professional (PMP) Certification
    # \end{itemize}

    # \end{document}
# """


# This function is used to send the user's info to ChatGPT in order to create the résumé info, the result is given in LaTeX code
def callGPT():
    prompt = 'first name is ' + fname + ' last name is ' + lname + ',  email is '+ email + ',  phone is ' + phone + ',  linkedin website is' + linkedin  + ', summary is ' + intro + ', i studied at ' + education + ',  work experience is ' + work + ', skills ' + skills + ', my projects ' + projects + ', my certifications ' + certs + '. using this info, make a résumé in latex form. Dont add any info that wasnt mentioned before and make it look really nice and attractive. no profile pic i want code only dont say anything else'
    model = "gpt-3.5-turbo-instruct"
    response = openai.Completion.create(model=model, prompt=prompt, max_tokens = 500)
    global generated_text
    generated_text = response.choices[0].text
    st.write(generated_text) # This part is used to see the code on the actual website, so this must be deleted
    print(generated_text) # This just prints the LaTeX code to the terminal
    return generated_text # Returned in order to use this for a rewrite, which is a Work in Progress


# This function is used to process the LaTeX code from ChatGPT and convert it into a PDF File
def PDFlatex(latex_code, output_file):
    latex_file = 'résumé.tex'
    with open(latex_file, 'w') as file:
        file.write(latex_code)
    subprocess.run([PDFpath, '-output-directory', '.', latex_file], check=True)
    subprocess.run(['mv', 'résumé.pdf', output_file], check=True)

# This function is used to process the LaTeX code from ChatGPT and convert it into a Word File
def DOClatex(latex_code, output_file):
    latex_file = 'résumé.tex'
    with open(latex_file, 'w') as file:
        file.write(latex_code)
    subprocess.run([DOCpath, '-s', latex_file, '-t', 'docx', '-o', 'résumé.docx'], check=True)
    subprocess.run(['mv', 'résumé.docx', output_file], check=True)


#If statement to create the résumé in either Word or PDF
if submitted == True and option == "Word":
    callGPT()
    pdfname = fname.capitalize() + ' ' + lname.capitalize() +"'s Résumé.docx"
    DOClatex(generated_text, pdfname)
    with open(pdfname, "rb") as file:
        PDFbyte = file.read()
    st.download_button(label=pdfname, data=PDFbyte, file_name=pdfname)
elif submitted == True and option == "PDF":
    callGPT()
    pdfname = fname.capitalize() + ' ' + lname.capitalize() +"'s Résumé.pdf"
    PDFlatex(generated_text, pdfname)
    with open(pdfname, "rb") as file:
        PDFbyte = file.read()
    st.download_button(label=pdfname, data=PDFbyte, file_name=pdfname)





#### WORK IN PROGRESS ####
# This is to add extra info to the résumé if the user feels like they don't like it that much
# with st.form("Extra Info"):
#     specify = st.text_input('Need Improvements? Put in specifics here for a better version!') # Work in Progress
#     submit = st.form_submit_button("Submit")

# def rewriteGPT():
#     generated_text = callGPT()
#     prompt = 'Make this LaTeX code ' + generated_text + 'better according to' + specify + 'dont any any extra info. dont forget begin document and end document'
#     model = "gpt-3.5-turbo-instruct"
#     response = openai.Completion.create(model=model, prompt=prompt, max_tokens = 500)
#     global new_text
#     new_text = response.choices[0].text

# if submit == True and option == "Word":
#     rewriteGPT()
#     pdfname = fname.capitalize() + ' ' + lname.capitalize() +"'s Résumé.docx"
#     DOClatex(new_text, pdfname)
#     with open(pdfname, "rb") as file:
#         PDFbyte = file.read()
#     st.download_button(label=pdfname, data=PDFbyte, file_name=pdfname)
# elif submit == True and option == "PDF":
#     rewriteGPT()
#     pdfname = fname.capitalize() + ' ' + lname.capitalize() +"'s Résumé.pdf"
#     PDFlatex(new_text, pdfname)
#     with open(pdfname, "rb") as file:
#         PDFbyte = file.read()
#     st.download_button(label=pdfname, data=PDFbyte, file_name=pdfname)
