''' Blog that uses the Flask micro web framework and the Bootstrap css framework
to load blog posts from an api and send emails from the contact form.  '''
from os import getenv
import smtplib
from dotenv import load_dotenv
from flask import Flask, render_template, request
import requests


load_dotenv()

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get(
    "https://api.npoint.io/c790b4d5cab58020d391", timeout=10).json()

# email details
PASSWORD = getenv('password')
MY_EMAIL = getenv('my_email')
HOST = "smtp.gmail.com"
SEND_TO = getenv('send_to')

''' To set up your google email to allow an app to send emails Go to https://myaccount.google.com/
Select Security on the left and scroll down to How you sign in to Google
Enable 2-Step Verification
Click on 2-Step Verification again, and scroll to the bottom.
There you can add an App password.
Use this as the password for smtplib.SMPT login'''


def send_mail(host, user_email, password, send_to, message):
    '''  send email given host, user, password, email recipient, and message '''
    with smtplib.SMTP(host) as connection:
        connection.starttls()  # transport layer security port 587
        connection.login(user=user_email, password=password)
        connection.sendmail(
            from_addr=user_email,
            to_addrs=send_to,
            msg=message)


app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        subject = "Subject:Message from MyBlog\n\n"
        send_mail(HOST, MY_EMAIL, PASSWORD, SEND_TO, message=subject+message)
        return render_template('contact.html',
                               method="post",
                               name=name,
                               email=email,
                               phone=phone,
                               message=message)

    return render_template('contact.html', method="get")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
