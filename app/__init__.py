import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

menu_items = [
    {"name": "Home", "url": "/"},
    {"name": "Hobbies", "url": "/hobbies"},
    {"name": "Experience", "url": "/experience"},
    {"name": "Education", "url": "/education"},
    {"name": "Travel", "url": "/wib"}
    ]

hobby_items = [
    {"name": "Climbing", "duration": "1+ years", "description": "I have been on and off climbing for the past year with the hardest grade I have ever climbed being a V6 although I hope to improve.", "img": "../static/img/climb.jpg"},
    {"name": "Lifting", "duration": "5+ years", "description": "I have been lifting for a while now, although I have been more focused on climmbing as of recent I still try to make time for lifting sessions!",  "img": "../static/img/weights.jpg"}
]

experience_items = [
    {"name": "MLH Fellowship", "When": "Summer 2025", "Company_URL": "https://fellowship.mlh.io/",  "Accomplished": "I was able to improve my skills with technologies such as github and git aswell as learn more about exisiting technologies such as Linux.", "img": "../static/img/mlh_fellow.jpg"},
    {"name": "Dive Lab", "When": "Summer 2025", "Company_URL": "https://github.com/divelab", "Accomplished": "I was able to get hands on experience working with LLMs and there use cases within material science as I worked on improving models using reinforcement learning and prompt engineering.", "img": "../static/img/dive_logo.jpg"}
]

education_items = [
    {"name": "Texas A&M", "Level": "Undergrad", "Enrollment": "2024 - 2028", "Status": "Current", "img": "../static/img/tamu_logo.jpg"},
    {"name": "Ronald Reagan High School", "Level": "Secondary School", "Enrollment": "2020 - 2024", "Status": "Completed", "img": "../static/img/rrhs.jpg"}
]

where_i_been = [{"name": "San Antonio", "coords": [29.4241, -98.4936]}, 
                {"name": "Dallas", "coords": [32.7767, -96.7970]}, 
                {"name": "Houston", "coords": [29.7604, -95.3698]}, 
                {"name": "Los Angeles", "coords": [34.0522, -118.2437]},
                {"name": "Pensacola", "coords": [30.4213, -87.2169]}, 
                {"name": "New Orleans", "coords": [29.9511, -90.0715]},
                {"name": "Austin", "coords": [30.2672, -97.7431]}, 
                {"name": "Dublin", "coords": [53.3498, -6.2603]},
                {"name": "London", "coords": [51.5074, -0.1278]},
                {"name": "Tokyo", "coords": [35.6895, 139.6917]},
                {"name": "San Jose", "coords": [9.9281, -84.0907]}, 
                {"name" : "Phoenix", "coords": [33.4484, -112.0740]}]

@app.route('/')
def index():
    return render_template('index.html', title="Declan's Portfolio", url=os.getenv("URL"), menu=menu_items)

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Declan's Hobbies", url=os.getenv("URL"), menu=menu_items, hobby=hobby_items)

@app.route('/experience')
def experience():
    return render_template('experience.html', title="Declan's Experience", url=os.getenv("URL"), menu=menu_items, experiences=experience_items)

@app.route('/education')
def education():
    return render_template('education.html', title="Declan's Education", url=os.getenv("URL"), menu=menu_items, educations = education_items)

@app.route('/wib')
def wib():
    return render_template('wib.html', title="Where I've Been", url=os.getenv("URL"), menu=menu_items, where_i_been = where_i_been)


if __name__ == '__main__':
    app.run(debug=True)
