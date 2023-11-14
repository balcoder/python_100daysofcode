from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[
                        DataRequired(), Email(message="Not a valid email, format must be: joe@blogs.com")])
    password = PasswordField(label='Password', validators=[
                             DataRequired(), Length(min=8, message='Password must be at least 8 characters long')])
    submit = SubmitField(label='Login')


app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.secret_key = ";jfipierfwee99303o9"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template('/success.html')
        else:
            return render_template('/denied.html')

    return render_template('login.html', form=login_form)


@app.route("/success")
def success():
    return render_template('success.html')


@app.route('/denied')
def denied():
    return render_template('denied')


if __name__ == '__main__':
    app.run(debug=True)
