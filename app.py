from flask import Flask
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # Adds the project folder to path

from textbook_shi import project_or_smth
app = Flask(__name__)

def run_project():
    os.system("python textbook_shi/project_or_smth.py")  # Runs thefile
    return "Project executed!"


if __name__ == "__main__":
    app.run(debug=True)



