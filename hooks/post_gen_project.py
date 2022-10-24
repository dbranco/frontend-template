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

if os.environ.get('HOST_USER_ID', '0') != '0' and os.environ.get('HOST_GROUP_ID', '0') != '0':
    subprocess.check_call('chown -R $HOST_USER_ID:$HOST_GROUP_ID $(pwd)', shell=True)
