from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(_name_)
CORS(app)

# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/courseSystemDB"  # Change this if needed
mongo = PyMongo(app)

# JWT Configuration
app.config['JWT_SECRET_KEY'] = 'super_secret_key'  # Change this to something secure
jwt = JWTManager(app)

bcrypt = Bcrypt(app)

# User Schema for Sign Up and Sign In
@app.route('/signup', methods=['POST'])
def signup():
    email = request.json.get('email')
    password = request.json.get('password')

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    try:
        mongo.db.users.insert_one({'email': email, 'password': hashed_password})
        return jsonify(message="User created"), 201
    except Exception as e:
        return jsonify(message="Error creating user", error=str(e)), 500

# Sign In Route
@app.route('/signin', methods=['POST'])
def signin():
    email = request.json.get('email')
    password = request.json.get('password')

    user = mongo.db.users.find_one({'email': email})
    
    if user and bcrypt.check_password_hash(user['password'], password):
        access_token = create_access_token(identity=user['_id'])
        return jsonify(access_token=access_token), 200
    else:
        return jsonify(message="Invalid credentials"), 401

# Teacher Profile Route
@app.route('/teachers', methods=['GET'])
@jwt_required()
def get_teachers():
    teachers = list(mongo.db.teachers.find())
    return jsonify(teachers), 200

# Route to submit course selection
@app.route('/courses', methods=['POST'])
@jwt_required()
def submit_courses():
    current_user = get_jwt_identity()
    theory_courses = request.json.get('theoryCourses')
    lab_courses = request.json.get('labCourses')

    try:
        mongo.db.course_selection.insert_one({
            'studentId': str(current_user),
            'theoryCourses': theory_courses,
            'labCourses': lab_courses
        })
        return jsonify(message="Course selection saved"), 201
    except Exception as e:
        return jsonify(message="Error saving course selection", error=str(e)), 500

if _name_ == '_main_':
    app.run(debug=True)