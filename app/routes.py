from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route("/")
@app.route("/index")
def index():
	user = {"username":"Octavian"}
	posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

	return render_template("index.html", title="Home"	, user=user, posts=posts)

@app.route("/contact")
def contact():
	return render_template("contact.html", title="Contact")

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remembre_me={}'.format(form.username.data, form.remember_me.data))
        print('Login requested for user {}, remembre_me={}'.format(form.username.data, form.remember_me.data))
        redirect("/index")
    return render_template("login.html", title="Log In", form = form)