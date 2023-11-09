import requests
from flask import Flask, render_template

# get the blog data from npoint.io
response = requests.get(
    "https://api.npoint.io/bc737a3039b048f93927", timeout=10)
blog_data = response.json()

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', blog_data=blog_data)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/posts')
def posts():
    return render_template('posts.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/blog/<id>')
def blog(id):

    return render_template('posts.html', id=id, blog_data=blog_data[int(id)-1])


if __name__ == "__main__":
    app.run(debug=True)
