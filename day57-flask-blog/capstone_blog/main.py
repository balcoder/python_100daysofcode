import requests
from flask import Flask, render_template


app = Flask(__name__)

blog_api = "https://api.npoint.io/c790b4d5cab58020d391"
blog_data = requests.get(blog_api, timeout=10).json()


@app.route('/')
def home():   

    return render_template("index.html", blog_data=blog_data)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    post_data = None
    for post in blog_data:
        if post['id'] == post_id:
            post_data = post 
    return render_template('post.html', post_data=post_data)

if __name__ == "__main__":
    app.run(debug=True)
