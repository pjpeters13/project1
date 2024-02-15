from flask import Flask, render_template, request, redirect
import webbrowser
import os
import subprocess

app = Flask(__name__)

def display_project_description():
    project_description = """
    <html>
    <head>
    <style>
    body {
        background-color: black;
        color: white;
        text-align: center;
    }
    </style>
    </head>
    <body>
    <h1>Welcome to the Crime Data Analysis Project!</h1>
    <p>This project analyzes NYC crime data from 2010 to 2022, uncovering patterns across boroughs and time.</p>
    <p>Choose an option below:</p>
    <p>Note! This page is in the beta phase and will serve as a dashboard for this project</p>
    <form action="/choice" method="post">
    <input type="radio" name="choice" value="1"> View PowerPoint presentation (link)<br>
    <input type="radio" name="choice" value="2"> Run data collection script: Data_Prep/geting_data.ipynb<br>
    <input type="radio" name="choice" value="3"> Run file browser for analysis files: Data_Analysis/selektor.ipynb<br>
    <input type="submit" value="Submit">
    </form>
    </body>
    </html>
    """

    return project_description

@app.route('/')
def index():
    return display_project_description()

@app.route('/choice', methods=['POST'])
def process_choice():
    choice = request.form['choice']
    
    if choice == "1":
        # Replace 'link_to_powerpoint_presentation' with the actual link
        link_to_powerpoint_presentation = "https://www.canva.com/design/DAF8r-QMA3Q/fRnDEgUW1yXzFsSdYsAsHw/edit?utm_content=DAF8r-QMA3Q&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton"
        return redirect(link_to_powerpoint_presentation)
    elif choice == "2":
        return "Option 2 is still in beta phase. It is recommended to open files from the Data_Prep folder in your Jupyter notebook."
    elif choice == "3":
        return "Option 3 is still in beta phase. It is recommended to open files from the Data_Analysis folder in your Jupyter notebook."
    else:
        return "Invalid choice. Please enter 1, 2, or 3."


if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000/')
    app.run(debug=False)
