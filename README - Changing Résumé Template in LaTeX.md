# README

## Instructions on how to alter the Résumé Templates

### Step 1: Downloading the files
Before starting, make sure that the templates are already downloaded on your computer to ensure that the previous templates don't change. Download the example résumés as well, in order to see a quick 

### Step 2: Open the LaTeX file up
Open up the .tex files using TeXShop (Mac) or TeXworks (Windows), or Overleaf. 
- If you choose to use Overleaf, you have to go to the [Overleaf Website](https://www.overleaf.com) and create an account. From there, you will be able to import .tex files in order to get started.

- If you choose to install one of the apps, the instructions for installation are provided in the "README - Start Here.md" file.

After you have selected your desired .tex editor, open the file and take a look at it. Using Template 2 as an example, if you want to create another section, you can use \section{section name}. Once you have typed that in, start a new line and type in either \cventry{}{}{}{}{}{} or \cvitem{}{}. Use cventry for something like work experince and use cvitem for skills, certifications, etc. If you are using \cventry, make sure to put \vspace{-\baselineskip} in the line above and putting Once you have chosen which one you want copy and paste "\fontsize{11}{12}\selectfont" into the last {} for cventry. This alters spacing and font issues for the beginning.

Additionally, you can change the TYPE of template it is. Tor templates 2 and 3, you can change the second line's {} value to 5 different types: casual, classic, oldstyle, banking or fancy.

Keep in mind that banking and classic have been used in templates 2 and 3. Along with that, you can change the color from blue to: black, blue, burgundy, green, grey, orange, purple, red.

If you want to add any text, type in whatever you want. You must be in the LAST {} for cventry and cvitem. If you want your text bolded, put \textbf{} around that text. If you want it in italics, use \textit{} instead.

If you want to put something in bullet points, start off with a new line that says "\begin{itemize}". Start another new line, put a \item in front of it, then type in your info. To start a new bullet point, use \item. After you are done with your bullet points, make sure to end it using \end{itemize}. 

If you want your text in general to be in a new line, use \\ to start a new line. When creating your text, the characters "$ % # _ &" are classified as special characters. In order to keep them as text, put a "\" in front of them. For previewing your document:

TeXShop: Hit &#8984;T for the preview
MiKTeX: Click the green play button on the top left
Overleaf: &#8984;S or CTRL + S

That's it! You have completed an example résumé!

### Notes for Developers:
Once the example résumé has been created, make a new copy and rename it. After that, delete all text that was created for the new resume. For example:

\section{Projects}
\cvitem{}{Project Name: E-commerce Platform, Tech Solutions Inc.
Project Description: Led the development of a cutting-edge and highly adaptable e-commerce platform leveraging the power of Python, Django, and React. Spearheaded the implementation of robust payment gateways, advanced product recommendation algorithms, and state-of-the-art user authentication mechanisms. Ensured scalability and modularity of the platform to meet the ever-evolving needs of Tech Solutions Inc.}

becomes

\section{Projects}
\cvitem{}{varName}

Make sure to change "varName" to something else.