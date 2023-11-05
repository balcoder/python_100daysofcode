import random
import requests
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def home():
    random_number = random.randint(1,10)
    year = datetime.now().year
    return render_template('index.html', num=random_number, year=year)

@app.route("/guess/<name>")
def guess(name):
    genderize_url  = f"https://api.genderize.io?name={name}"
    agify_url = f"https://api.agify.io?name={name}"
    gender_data = requests.get(genderize_url, timeout=10).json()
    age_data = requests.get(agify_url, timeout=10).json()    
    return render_template('index.html', name=name, gender_data=gender_data, age_data=age_data)

@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url, timeout=10)
    posts = response.json()
    print(posts)
    return render_template('blog.html', all_posts=posts)

if __name__ == "__main__":
    app.run(debug=True)
