from flask import Blueprint, redirect, render_template, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .model import User,db
from .model_admin import Admin, db

auth = Blueprint('auth', __name__)

@auth.route('/')
def home():
    return render_template('home.html')

@auth.route('/login')
def login():
    return render_template('login.html')

#*********** ADMIN *************

@auth.route('/admin/login')
def admin_login():
    return render_template('admin/auth/login.html')

@auth.route('/admin/signup')
def admin_signup():
    return render_template('admin/auth/register.html')

@auth.route('/admin/logout')
@login_required
def admin_logout():
    logout_user()
    return redirect(url_for('main.shopping'))


@auth.route('/admin/login', methods=['POST'])
def login_admin():
    email = request.form.get('email')
    password = request.form.get('password')
    remember=True if request.form.get('remember') else False
    user= Admin.query.filter_by(email=email).first()
    #print(email,check_password_hash(user.password,password))
    if not user or not check_password_hash(user.password,password):
        flash("Login failed try again")
        return redirect(url_for('auth.admin_login'))
    login_user(user, remember=remember)
    flash("Welcome "+ current_user.username)
    return redirect(url_for('admin.dashboard'))

@auth.route('/admin/signup', methods=['POST'])
def signup_admin():
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    hash_password=generate_password_hash(password, method = 'sha256')
    print(email, hash_password)
    user= Admin.query.filter_by(email=email).first()
    if user:
        flash("User Already exist try different email")
        return redirect(url_for('auth.admin_signup'))
    New_user=Admin(fname,lname,username,email,hash_password)
    db.session.add(New_user)
    db.session.commit()
    flash("Successfully created!!")
    return redirect(url_for('admin.dashboard'))

#******** ADMIN *********************


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember=True if request.form.get('remember') else False
    user= User.query.filter_by(email=email).first()
    #print(email,check_password_hash(user.password,password))
    if not user or not check_password_hash(user.password,password):
        flash("Login failed try again")
        return redirect(url_for('main.home'))
    login_user(user, remember=remember)
    flash("Welcome "+ current_user.username)
    return redirect(url_for('main.shopping'))

@auth.route('/signup')
def signup():
    return render_template('pages/auth/register.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    hash_password=generate_password_hash(password, method = 'sha256')
    print(email, hash_password)
    user= User.query.filter_by(email=email).first()
    if user:
        flash("User Already exist try different email")
        return redirect(url_for('auth.signup'))
    New_user=User(fname,lname,username,email,hash_password)
    db.session.add(New_user)
    db.session.commit()
    flash("Successfully created!!")
    return render_template('home.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.shopping'))