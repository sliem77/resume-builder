# README

## Prerequistes for everything

### Step 1: Install pandoc on your computer
Download [pandoc](https://github.com/jgm/pandoc/releases/tag/3.1.11.1) on your computer.

#### Installation for Windows: 
Download the .msi version and install it.

#### Installation for Mac:
Check your Mac type by clicking the apple logo on the top left, choosing "About This Mac" and the Chip should either say Intel or Apple M1 (or higher).

For Intel Macs: Download the x86_64-macOS.pkg and install it.

Silicon Macs: Download the arm64-macOS.pkg and install it.
    
You can check your type clicking the apple logo on the top left, choosing "About This Mac" and the Chip should either say Intel or Apple M1 (or higher)

### Step 2: Install pdflatex on your computer
For Windows users: Download [MiKTeX](https://miktex.org/download), scroll down and click Windows tab, then click the blue download button.

For Mac users: Download [Homebrew](https://github.com/Homebrew/brew/releases/tag/4.2.8) and download the .pkg file. Once you have downloaded that, open up your terminal and type in: brew install --cask mactex

## Step 3 (Windows Only):
Open up the MiKTeX console, go to Packages, and in the "Install In" text box, type in currfile. There should be 3 options called: currfile, currfile_doc, and currfile_source. Select all of these and install them.