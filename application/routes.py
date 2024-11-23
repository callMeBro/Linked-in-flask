from application import app
from flask import render_template, redirect, url_for, request
from flask_login import login_user

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/courses')
def courses():
    return render_template('courses.html')


@app.route('/register')
def register():
    # registration logic here
    return render_template('register.html')




@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login logic (e.g., check username/password)
        # Assuming you have a User model and session handling
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('index'))  # Redirect to a page after login
        else:
            # Handle failed login attempt
            pass
    return render_template('login.html')
