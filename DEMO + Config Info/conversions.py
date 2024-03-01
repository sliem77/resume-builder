from config import *
from DEMO import *
import subprocess

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
