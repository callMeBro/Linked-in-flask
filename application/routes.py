from application import app, db, api
import json 
from flask import render_template, redirect, url_for, request, Response, jsonify
from flask_login import login_user
from mongoengine import connect
from application.models import User, Course, Enrollment 
from flask_restplus import Resource
    
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", login=True)

@app.route('/courses')
@app.route('/courses/<term>')
def courses(term="2019"):
    return render_template('courses.html', courseData=courseData, courses = True, term=term)


@app.route('/register')
def register():
    # registration logic here
    return render_template('register.html', login=True)

@app.route('/enrollment', methods=["GET", "POST"])
def enrollment():
    id = request.args.get('courseID')
    title = request.args.get('title')
    term = request.args.get('term')
    # registration logic here
    return render_template('enrollment.html', enrollment=True, data={"id":id, "title":title, "term":term})



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


courseData = [{"courseID":"1111","title":"PHP 101","description":"Intro to PHP","credits":3,"term":"Fall, Spring"}, {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":4,"term":"Spring"}, {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":3,"term":"Fall"}, {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":3,"term":"Fall, Spring"}, {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":4,"term":"Fall"}]

########################################################################################

@api.route('/api', '/api/')
class GetandPost(Resource):
    
    def get(self):
        return jsonify(User.objects.all())

@api.route('/api/<idx>')
class GetUpdateDelete(Resource):
    
    def post(self, idx):
        return jsonify(User.objects.all(user_id=idx))
    
    

########################################################################################
print(courseData[0]["title"])
    
@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if(idx == None):
        jdata = courseData
    else:
        jdata = courseData[int(idx)]
        
    return Response(json.dumps(jdata), mimetype="application/json" )   
        
        
        
class User(db.Document):
    user_id = db.IntField(unique=True)
    first_name = db.StringField( max_length=50)
    last_name = db.StringField( max_length=50)
    email = db.StringField( max_length=30 )
    password = db.StringField( max_length=30 )
    # Optionally, you can explicitly specify the collection name
    meta = {'collection': 'user'}
    
    
    
@app.route("/user")
def user():
    # Get the maximum user_id currently in the database
    max_user_id = User.objects.order_by('-user_id').first().user_id if User.objects.count() > 0 else 0

    # Create new users with unique IDs
    User(user_id=max_user_id + 1, first_name='Christian', last_name='Dean', email="christian@uta.com").save()
    User(user_id=max_user_id + 2, first_name='Sally', last_name='Smith', email="sally@uta.com").save()

    print(User._get_collection_name())

    # Fetch all users to display in the template
    users = User.objects.all()
    return render_template("user.html", users=users)
        