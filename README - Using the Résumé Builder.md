# README
## Before starting, please read the README - Start Here.md file
## Instructions for using the Résumé Builder

### Step 1: Download Visual Studio Code
Download [Visual Studio](https://code.visualstudio.com/download) and choose your platform. Once the installer is downloaded, open it up and follow the instructions to download Visual Studio Code.

### Step 2: Obtain an API Key from OpenAI
Go to the [OpenAI Website](https://platform.openai.com). Once you are there, click the Log in button. Login using your credentials. If you don't have an account, create one. Once you're logged in, on the left side will be a little lock symbol which will lead you to the API Keys. Click create new secret key. Make sure to copy down the API Key somewhere, you will only be able to see it one time.

### Step 3: Downloading the files
From Dropbox, download the "Config Info" Folder. This can be done by copying the folder and pasting it into Downloads.

### Step 4: Open Visual Studio Code + Configs
Open up Visual Studio and click on the "Open Folder" option. Find and select the Config Info folder. Open DEMO_v2.py and Config.py only.
    
From the files, open up Config.py and change api_key to your OpenAI api key, PDFpath to your pdflatex installation, and DOCpath to your pandoc installation. Once that is completed, you open up DEMO_v2.py.

    For Windows Users: 
        The path for pdflatex should be: C:\Users\Lenovo\AppData\Local\Program\MiKTeX\miktex\bin\x64\pdflatex, Lenovo is the base username for Lenovo computers, change it to your actual username if you don't have a Lenovo computer.
        The Path for pandoc should be: C:\Users\YourUserName\AppData\Local\Pandoc
        Once you have pasted the paths in, add in an extra "\" after each \, for example, becomes 
        "C:\\Users\\Lenovo\\AppData\\Local\\Program\\MiKTeX\\miktex\\bin\\x64\\pdflatex"

    For Mac Users, the paths provided in config.py should be correct. If not, open Finder, click on Go in the menu bar, click on Go to Folder, and type in:
        /usr/local/texlive/ to find pdflatex
        /opt/homebrew/ to find pandoc
        Use the Paths provided to navigate through your folders.

### Step 5: Launching the Résumé Builder
    Once you have opened the builder, open up the terminal from Visual Studio, which is on the top of  and go to the Config Info directory. Once you are there, copy and paste ALL of the pip commands in the VS Code Terminal:
    pip install streamlit
    pip install streamlit-image-select
    pip install openai==0.28
    pip install pdf2image
    
Once this is done, follow the [instructions](https://pdf2image.readthedocs.io/en/latest/installation.html) for your specific device.
    
After this, run "streamlit run DEMO_v2.py". This will launch your browser.

### Step 6: Using the Résumé Builder
In the program, choose any template you want. You can preview each template below the options. Once you have chosen your template, you can type in your information or use the default information provided in the text boxes.
    
For windows: If you see a popup saying package installation with files ending in .sty, hit install. Additionally, if you hit an error saying: shipbox:D, delete the existing pdf file.