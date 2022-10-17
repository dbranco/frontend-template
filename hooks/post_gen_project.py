import os
from pathlib import Path
import glob
import subprocess

REMOVE_FILES =[
     {% if cookiecutter.flavor == "javascript" %}
        '*.ts', '*.tsx', 'tsconfig.json'
     {% elif cookiecutter.flavor == "typescript" %}
        '*.js', '*.jsx'
     {% endif %}
]

for fileExtension in REMOVE_FILES:
    fileList = glob.glob(os.getcwd()+'/**/'+fileExtension, recursive=True)
    for filePath in fileList:
        if ('webpack.config.js' not in filePath):
            try:
                os.remove(filePath)
            except:
                print("Error while deleting file : ", filePath)

subprocess.check_call('npm i', shell=True)
