#pip install streamlit
#pip install streamlit-image-select
#pip install openai
#pip install pdf2image

#importing all necessary packages
from config import *
from streamlit_image_select import image_select
from pdf2image import convert_from_path
import streamlit as st
import openai
import subprocess
openai.api_key = api_key

st.title('Welcome to the Résumé Builder!')
tPaths = [t1, t2, t3] #t1, t2, t3 are the templates that are in the dropbox folder
x = 0 # simple counter for naming scheme

#function to display pdfs
def display_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    for i, image in enumerate(images):
        st.image(image, use_column_width=True)

st.text("Please Enter in your Information")
with st.form("Information"):
    rTemplates = image_select("Please Choose a Template", [img1, img2, img3]) #img1, img2, img3 are pics of the templates in dropbox
    
    #Loop is for the template naming scheme
    for path in tPaths:
        if x == 0:
            title = "Template 1"
        elif x == 1:
            title = "Template 2"
        else:
            title = "Template 3"
        with st.expander(f"View {title}"):
            display_pdf(path)
        x += 1
    #The following is putting a title with a default description in the second parameter. Second parameter must be deleted afterwards.
    fname = st.text_area("First Name", "Jeefe")
    lname = st.text_area("Last Name", "Comp")
    emails = st.text_area("Email", "Jefecomp@gmail.com")
    phones = st.text_area("Phone Number", "123-456-7890")
    linkedin = st.text_area("LinkedIn URL", "linkedin.com/in/jeefecomp")
    intro = st.text_area("Professional Summary", "Versatile and results-driven software engineer with expertise in full-stack web development, specializing in Python and Django. Proven track record of delivering high-impact projects and collaborating effectively within cross-functional teams. Dedicated to designing scalable solutions and passionate about solving complex problems.")
    education = st.text_area("Education", "2015 - 2019 Bachelor of Science in Computer Science, University of XYZ, City, Country")
    work = st.text_area("Work Experience", """2019-Present Software Engineer, Tech Solutions Inc., City, Country
○ Developed and maintained web applications using Python, Django, and JavaScript, delivering feature-rich and responsive
user interfaces.
○ Led the implementation of a modular and scalable e-commerce platform, resulting in a 20
○ Conducted code reviews, provided mentorship to junior developers, and actively participated in continuous improvement
initiatives.
2017-2019 Intern, Software Development, ABC Tech, City, Country
○ Contributed to the design and development of new software features, demonstrating proficiency in Java, JavaScript, and
SQL.
○ Assisted in the implementation of a data analytics tool, enabling the team to gain valuable insights into user behavior.
2016 - 2017 IT Support Specialist, XYZ Company, City, Country
○ Provided technical support to end-users, diagnosing and resolving hardware and software issues in a timely manner.
○ Implemented system upgrades and maintenance procedures, ensuring optimal performance of computer systems.""")
    skills = st.text_area("Skills", "Programming: Python, JavaScript, Java Web Frameworks: Django, React Database: MySQL, PostgreSQL Version Control: Git Tools: Docker, Jenkins Soft Skills: Team Collaboration, Problem Solving, Communication")
    projects = st.text_area("Projects", """E-commerce Platform, Tech Solutions Inc., City, Country
○ Led the development of a scalable and modular e-commerce platform using Python, Django, and React.
○ Implemented secure payment gateways, product recommendation algorithms, and enhanced user authentication mechanisms.""")
    certs = st.text_area("Certifications", "Certified Python Developer (XYZ Certification)")
    #option = st.radio(label = "What format do you want your résumé in?", options = ["Word", "PDF"])
    submitted = st.form_submit_button("Submit")

#Below are the templates in LaTeX, template1-3 is with dummy data and t1var-3 is the variables only version
template1 = r"""\documentclass[a4paper,10pt]{article}
\usepackage[left=0.5in, right=0.5in, top=0.5in, bottom=0.5in]{geometry}
\usepackage{enumitem}
\usepackage{parskip}
\usepackage{titlesec}

\titleformat{\section}{\large\bfseries}{\thesection}{1em}{}[{\titlerule[0.7pt]}]

\begin{document}

\pagestyle{empty}

\begin{center}
    \textbf{\LARGE John Doe} \\
    123 Main Street, Cityville, State ZIP Code | (555) 555-5555 | john.doe@email.com | LinkedIn: linkedin.com/in/johndoe
\end{center}

\section*{Objective}
Experienced Mechanical Engineer with a decade of expertise in designing and implementing innovative solutions. Proven track record of success in project management, team leadership, and delivering high-quality engineering solutions. Seeking a challenging role to contribute technical acumen and managerial skills.

\section*{Professional Experience}

\textbf{Senior Mechanical Engineer | XYZ Engineering Solutions, Cityville, USA | 2018-2022}
\begin{itemize}[left=0.5in]
    \item Led a team of 10 engineers in designing and executing projects, resulting in a 20\% increase in overall project efficiency.
    \item Developed and implemented cost-effective design modifications, reducing production costs by 15\%.
    \item Conducted feasibility studies and collaborated with cross-functional teams to ensure project success.
\end{itemize}

\textbf{Mechanical Design Engineer | ABC Manufacturing, Townsville, USA | 2015-2018}
\begin{itemize}[left=0.5in]
    \item Led the design and development of a new product line, increasing company revenue by 25\%.
    \item Implemented Lean Manufacturing principles, resulting in a 30\% reduction in production cycle time.
    \item Collaborated with suppliers to source cost-effective materials, reducing project costs by 10\%.
\end{itemize}

\textbf{Project Engineer | DEF Technology Innovations, Riverside, USA | 2012-2015}
\begin{itemize}[left=0.5in]
    \item Managed the entire project lifecycle, from conception to delivery, ensuring adherence to timelines and budgets.
    \item Conducted thorough risk assessments and implemented mitigation strategies, resulting in a 15\% reduction in project delays.
    \item Provided technical expertise and support to cross-functional teams, fostering collaboration and innovation.
\end{itemize}

\textbf{Junior Mechanical Engineer | GHI Engineering Services, Cityville, USA | 2010-2012}
\begin{itemize}[left=0.5in]
    \item Assisted in the design and testing of mechanical components for various projects.
    \item Conducted detailed analysis and troubleshooting, contributing to the resolution of complex technical issues.
    \item Collaborated with senior engineers to streamline design processes and improve overall project efficiency.
\end{itemize}

\textbf{Mechanical Intern | JKL Innovations, Cityville, USA | Summer 2009}
\begin{itemize}[left=0.5in]
    \item Assisted in the development of prototypes and performed testing of mechanical systems.
    \item Contributed to the analysis of design specifications and participated in team meetings to discuss project progress.
\end{itemize}

\section*{Skills}
\begin{flushleft}
\begin{itemize}[left=0.5in]
    \item SolidWorks, AutoCAD, and other CAD software proficiency, Finite Element Analysis (FEA), Prototyping and testing
\end{itemize}
\end{flushleft}

\section*{Education}
\textbf{Bachelor of Science in Mechanical Engineering} \\
University of Engineering, Cityville, USA | Graduated: 2010

\section*{Certifications}
\begin{itemize}[left=0.5in]
    \item Professional Engineer (PE) License
    \item Project Management Professional (PMP) Certification
\end{itemize}

\end{document}
"""
template2 = r"""\documentclass[11pt, a4paper, sans]{moderncv}

\moderncvstyle{banking} % Choose the style, e.g., 'casual', 'classic', 'banking', 'oldstyle', or 'fancy'.
\moderncvcolor{blue} % Choose the color scheme, e.g., 'black', 'blue', 'burgundy', 'green', 'grey', 'orange', 'purple', or 'red'.

% Adjust the page margins.
\usepackage[scale=0.9]{geometry}

% Personal Information
\fname{John}{Doe}
\emails{johndoe@example.com}
\phones{123-456-7890}
\social[linkedin]{linkedin.com/in/johndoe}

\begin{document}

\makecvtitle

\section{Professional Summary}
Results-driven and highly skilled software engineer with a passion for creating efficient and scalable solutions. Proven expertise in full-stack web development using Python and Django. Strong collaborator with a keen ability to solve complex problems.

\section{Education}
\cventry{}{Bachelor of Science in Computer Science}{University of XYZ}{City, Country}{}{}

\section{Work Experience}
\cventry{}{Software Engineer}{Tech Solutions Inc.}{City, Country}{Present}{
    \begin{itemize}
        \item Developed and maintained web applications using Python, Django, and JavaScript.
        \item Collaborated with cross-functional teams to deliver feature-rich and responsive user interfaces.
        \item Led the implementation of a modular and scalable e-commerce platform, resulting in a 20% increase in sales.
    \end{itemize}
}

\cventry{}{Intern, Software Development}{ABC Tech}{City, Country}{2019--2020}{
    \begin{itemize}
        \item Contributed to the design and development of new software features using Java and JavaScript.
        \item Assisted in the implementation of a data analytics tool, providing valuable insights into user behavior.
    \end{itemize}
}

\cventry{}{IT Support Specialist}{XYZ Company}{City, Country}{2018--2019}{
    \begin{itemize}
        \item Provided technical support to end-users, diagnosing and resolving hardware and software issues.
        \item Implemented system upgrades and maintenance procedures for optimal performance.
    \end{itemize}
}

\section{Skills}
\cvitem{}{Python, Django, JavaScript, Java, Git, Docker}

\section{Projects}
\cvitem{}{E-commerce Platform: Led the development of a scalable and modular e-commerce platform using Python, Django, and React. Implemented secure payment gateways, product recommendation algorithms, and enhanced user authentication mechanisms.}

\section{Certifications}
\cvitem{}{Certified Python Developer (XYZ Certification)}

\end{document}
"""
template3 = r"""\documentclass[10pt, a4paper, sans]{moderncv}

\moderncvstyle{classic} % Choose the style, e.g., 'casual', 'classic', 'banking', 'oldstyle', or 'fancy'.
\moderncvcolor{blue} % Choose the color scheme, e.g., 'black', 'blue', 'burgundy', 'green', 'grey', 'orange', 'purple', or 'red'.

% Adjust the page margins.
\usepackage[scale=0.9]{geometry}

% Personal Information
\fname{John}{Doe}
\email{johndoe@example.com}
\phone{123-456-7890}
\social[linkedin]{linkedin.com/in/johndoe}

\begin{document}

\makecvtitle

\section{Professional Summary}
Versatile and results-driven software engineer with expertise in full-stack web development, specializing in Python and Django. Proven track record of delivering high-impact projects and collaborating effectively within cross-functional teams. Dedicated to designing scalable solutions and passionate about solving complex problems.

\section{Education}
\cventry{2015--2019}{Bachelor of Science in Computer Science}{University of XYZ}{City, Country}{}{}

\section{Work Experience}
\cventry{2019--Present}{Software Engineer}{Tech Solutions Inc.}{City, Country}{}{
\begin{itemize}
    \item Developed and maintained web applications using Python, Django, and JavaScript, delivering feature-rich and responsive user interfaces.
    \item Led the implementation of a modular and scalable e-commerce platform, resulting in a 20% increase in sales and improved user experience.
    \item Conducted code reviews, provided mentorship to junior developers, and actively participated in continuous improvement initiatives.
\end{itemize}
}

\cventry{2017--2019}{Intern, Software Development}{ABC Tech}{City, Country}{}{
\begin{itemize}
    \item Contributed to the design and development of new software features, demonstrating proficiency in Java, JavaScript, and SQL.
    \item Assisted in the implementation of a data analytics tool, enabling the team to gain valuable insights into user behavior.
\end{itemize}
}

\cventry{2016--2017}{IT Support Specialist}{XYZ Company}{City, Country}{}{
\begin{itemize}
    \item Provided technical support to end-users, diagnosing and resolving hardware and software issues in a timely manner.
    \item Implemented system upgrades and maintenance procedures, ensuring optimal performance of computer systems.
\end{itemize}
}

\section{Skills}
\textbf{Programming:} Python, JavaScript, Java \\
\textbf{Web Frameworks:} Django, React \\
\textbf{Database:} MySQL, PostgreSQL \\
\textbf{Version Control:} Git \\
\textbf{Tools:} Docker, Jenkins \\
\textbf{Soft Skills:} Team Collaboration, Problem Solving, Communication

\section{Projects}
\cventry{}{E-commerce Platform}{Tech Solutions Inc.}{City, Country}{}{
\begin{itemize}
    \item Led the development of a scalable and modular e-commerce platform using Python, Django, and React.
    \item Implemented secure payment gateways, product recommendation algorithms, and enhanced user authentication mechanisms.
\end{itemize}
}

\section{Certifications}
\cvitem{}{Certified Python Developer (XYZ Certification)}

\end{document}
"""

t1var = r"""\documentclass[a4paper,10pt]{article}
\usepackage[left=0.5in, right=0.5in, top=0.5in, bottom=0.5in]{geometry}
\usepackage{enumitem}
\usepackage{parskip}
\usepackage{titlesec}

\titleformat{{\section}}{{\large\bfseries}}{{\thesection}}{{1em}}{{}}[{{\titlerule[0.8pt]}}]

\begin{{document}}

\pagestyle{{empty}}

\begin{{center}}
    \textbf{{\LARGE {fname} {lname}}} \\
    {emails} | {phones} | LinkedIn: {linkedin}
\end{{center}}

\section*{{Objective}}
{intro}

\section*{{Professional Experience}}
{work}

\section*{{Skills}}
\begin{{flushleft}}
{skills}
\end{{flushleft}}

\section*{{Education}}
{education}

\section*{{Certifications}}
{certs}

\end{{document}}
"""
t2var = r"""\documentclass[11pt, a4paper, sans]{moderncv}

\moderncvstyle{banking} % Choose the style, e.g., 'casual', 'classic', 'banking', 'oldstyle', or 'fancy'.
\moderncvcolor{blue} % Choose the color scheme, e.g., 'black', 'blue', 'burgundy', 'green', 'grey', 'orange', 'purple', or 'red'.

% Adjust the page margins.
\usepackage[scale=0.9]{geometry}

% Personal Information
\name{\fname}}{\lname}}
\email{\emails}}
\phone{\phones}}
\social[linkedin]{\linkedin}}

\begin{document}

\makecvtitle

\section{Professional Summary}
{\intro}

\section{Education}
\cventry{}{\education}}{}{}{}{}

\section{Work Experience}
\cventry{}{\work}}{}{}{}{}

\section{Skills}
\cvitem{}{\skills}}

\section{Projects}
\cvitem{}{\projects}}

\section{Certifications}
\cvitem{}{\certs}}

\end{document}
"""
t3var = r"""\documentclass[11pt, a4paper, sans]{moderncv}

\moderncvstyle{classic} % Choose the style, e.g., 'casual', 'classic', 'banking', 'oldstyle', or 'fancy'.
\moderncvcolor{blue} % Choose the color scheme, e.g., 'black', 'blue', 'burgundy', 'green', 'grey', 'orange', 'purple', or 'red'.

% Adjust the page margins.
\usepackage[scale=0.9]{geometry}

% Personal Information
\name{\fname}{\lname}
\email{\emails}}
\phone{\phones}
\social[linkedin]{linkedin}

\begin{document}

\makecvtitle

\section{Professional Summary}
{\intro}

\section{Education}
\cventry{}{education}{}{}{}{}

\section{Work Experience}
\cventry{}{\work}{}{}{}{}

\section{Skills}
\cvitem{}{\skills}

\section{Projects}
\cvitem{}{\projects}

\section{Certifications}
\cvitem{}{\certs}

\end{document}
"""

#gptAns and resume_data are info that ChatGPT gives out, just putting them here as examples
gptAns = {
    "\fname": "Jeff",
    "\lname": "Comps",
    "\emails": "jef@comp.com",
    "\phones": "2635476432",
    "\linkedin": "Smith",
    "\intro": "Passionate and detail-oriented professional with a strong background in technology and a focus on delivering high-quality results. Effective communicator with excellent problem-solving skills.",
    "\education": [
        {
            "institution": "UIC (University of Illinois at Chicago)",
            "degree": "[Your Degree]",
            "major": "[Your Major]",
            "graduation_year": "[Your Graduation Year]"
        }
    ],
    "\work": [
        {
            "company": "Dell",
            "position": "[Your Position]",
            "duration": "[Start Date] - [End Date]",
            "responsibilities": "[Your Responsibilities and Achievements]"
        }
    ],
    "\skills": ["Java", "Python", "Hadoop"],
    "\projects": [
        {
            "name": "Computer Building",
            "description": "[Brief Description of the Project]",
            "technologies_used": "[Technologies Used]"
        }
    ],
    "\certs": "None"
}

resume_data = {
    'fname': 'Jeefe',
    'lname': 'Comp',
    'emails': 'Jefecomp@gmail.com',
    'phones': '123-456-7890',
    'linkedin': 'linkedin.com/in/jeefecomp',
    'intro': 'Versatile and results-driven software engineer with expertise in full-stack web development, specializing in Python and Django. Proven track record of delivering high-impact projects and collaborating effectively within cross-functional teams. Dedicated to designing scalable solutions and passionate about solving complex problems.',
    'education': '2015 - 2019 Bachelor of Science in Computer Science, University of XYZ, City, Country',
    'work': [
        {
            'position': 'Software Engineer',
            'company': 'Tech Solutions Inc., City, Country',
            'responsibilities': [
                'Developed and maintained web applications using Python, Django, and JavaScript, delivering feature-rich and responsive user interfaces.',
                'Led the implementation of a modular and scalable e-commerce platform, resulting in a 20% improvement in performance.',
                'Conducted code reviews, provided mentorship to junior developers, and actively participated in continuous improvement initiatives.'
            ],
            'duration': '2019-Present'
        },
        {
            'position': 'Intern, Software Development',
            'company': 'ABC Tech, City, Country',
            'responsibilities': [
                'Contributed to the design and development of new software features, demonstrating proficiency in Java, JavaScript, and SQL.',
                'Assisted in the implementation of a data analytics tool, enabling the team to gain valuable insights into user behavior.'
            ],
            'duration': '2017-2019'
        },
        {
            'position': 'IT Support Specialist',
            'company': 'XYZ Company, City, Country',
            'responsibilities': [
                'Provided technical support to end-users, diagnosing and resolving hardware and software issues in a timely manner.',
                'Implemented system upgrades and maintenance procedures, ensuring optimal performance of computer systems.'
            ],
            'duration': '2016 - 2017'
        }
    ],
    'skills': {
        'Programming': ['Python', 'JavaScript', 'Java'],
        'Web Frameworks': ['Django', 'React'],
        'Database': ['MySQL', 'PostgreSQL'],
        'Version Control': ['Git'],
        'Tools': ['Docker', 'Jenkins'],
        'Soft Skills': ['Team Collaboration', 'Problem Solving', 'Communication']
    },
    'projects': [
        {
            'name': 'E-commerce Platform',
            'company': 'Tech Solutions Inc., City, Country',
            'description': [
                'Led the development of a scalable and modular e-commerce platform using Python, Django, and React.',
                'Implemented secure payment gateways, product recommendation algorithms, and enhanced user authentication mechanisms.'
            ]
        }
    ],
    'certs': ['Certified Python Developer (XYZ Certification)']
}

def replace_tokens(template_file, output_file, replacements):
    with open(template_file, 'r') as f:
        template = f.read()

    for placeholder, value in replacements.items():
        if isinstance(value, list):
            value = ', '.join(map(str, value))
        template = template.replace(placeholder, str(value))

    with open(output_file, 'w') as f:
        f.write(template)

def PDFlatex(latex_code, output_file):
    latex_file = 'résumé.tex'
    with open(latex_file, 'w') as file:
        file.write(latex_code)
    subprocess.run([PDFpath, '-output-directory', '.', latex_file], check=True)
    subprocess.run(['mv', 'résumé.pdf', output_file], check=True)

# This function is used to send the user's info to ChatGPT in order to create the résumé info
# def callGPT():
#     prompt = 'here are my variables (in order): fname, lname, e_add, phones, linkedin, intro, education, work, skills, projects, certs. first name is ' + fname + ' last name is ' + lname + ',  email is '+ e_add + ',  phone is ' + phones + ',  linkedin website is' + linkedin  + ', summary is ' + intro + ', i studied at ' + education + ',  work experience is ' + work + ', skills ' + skills + ', my projects ' + projects + ', my certifications ' + certs + '. put this in a python dictionary and make the intro sound better:' + intro + ". replace the original 'intro' with the new one you made. use double quotes not single quotes. give the dictionary ONLY and nothing else dont put 'var_name = x' in the beginning, dont change variable names"
#     model = "gpt-3.5-turbo-instruct"
#     response = openai.Completion.create(model=model, prompt=prompt, max_tokens = 700)
#     ans = response.choices[0].text
#     global generated_text
#     generated_text = json.loads(ans)
#     st.write(generated_text)
#     return generated_text

if submitted == True:
    #callGPT()
    replace_tokens(temp2, output1, resume_data)
    PDFlatex(output1)


#OPTIONAL: If statement to create the résumé in either Word or PDF
# if submitted == True:
#     callGPT()
#     pdfname = fname.capitalize() + ' ' + lname.capitalize() +"'s Résumé.pdf"
#     PDFlatex(output1, pdfname)
#     with open(pdfname, "rb") as file:
#         PDFbyte = file.read()
#     st.download_button(label=pdfname, data=PDFbyte, file_name=pdfname)