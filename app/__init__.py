import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict
import hashlib
from urllib.parse import urlencode

load_dotenv()
app = Flask(__name__)
mydb = MySQLDatabase(   os.getenv("MYSQL_DATABASE"),
                        user=os.getenv("MYSQL_USER"),
                        password=os.getenv("MYSQL_PASSWORD"),
                        host=os.getenv("MYSQL_HOST"),
                        port=3306)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

menu_items = [
    {"name": "Home", "url": "/"},
    {"name": "Hobbies", "url": "/hobbies"},
    {"name": "Experience", "url": "/experience"},
    {"name": "Education", "url": "/education"},
    {"name": "Travel", "url": "/wib"},
    {"name": "Timeline", "url": "/timeline"}
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

@app.route('/timeline')
def timeline():
    timeline_posts = get_time_line_post()['timeline_posts']
    for post in timeline_posts:
        # Set your variables here
        email = post['email']
        default = "mp"
        size = 40
        
        # Encode the email to lowercase and then to bytes
        email_encoded = email.lower().encode('utf-8')
        
        # Generate the SHA256 hash of the email
        email_hash = hashlib.sha256(email_encoded).hexdigest()
        
        # Construct the URL with encoded query parameters
        query_params = urlencode({'d': default, 's': str(size)})
        gravatar_url = f"https://www.gravatar.com/avatar/{email_hash}?{query_params}"
        print(gravatar_url)
        post['img'] = gravatar_url
    return render_template('timeline.html', title="Timeline", url=os.getenv("URL"), menu=menu_items, timeline=timeline_posts)


@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in
            TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

if __name__ == '__main__':
    app.run(debug=True)
