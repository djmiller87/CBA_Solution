from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user, service, order
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login_register')
def login_register():
    return render_template('login.html')


@app.route('/register', methods=['POST'])
def register():
    if not user.User.validate_user(request.form):
        return redirect('/login_register')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data ={
        'business_name': request.form['business_name'],
        'email': request.form['email'],
        'password': pw_hash
    }
    user_id = user.User.save(data)
    session['user_id'] = user_id
    return redirect(f"/dashboard/{user_id}")

@app.route('/login', methods=['POST'])
def login():
    data = {'email': request.form['email']}
    user_in_db = user.User.get_by_email(data)
    print(data)
    if not user_in_db:
        flash("*Invalid Email/Password", 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("*Invalid Email/Password", 'login')
        return redirect('/login_register')
    session['user_id'] = user_in_db.id

    print(user_in_db.id)
    return redirect(f"/dashboard/{user_in_db.id}")

@app.route('/dashboard/<int:id>')
def dashboard(id):
    if session['user_id'] != id:
        return redirect('/')
    data = {
        'id' : id
    }
    one_user = user.User.one_user_info(data)
    gross = order.Order.gross_income(data)
    costs = order.Order.business_costs(data)
    worked_hours = order.Order.business_hours(data)
    all_orders = order.Order.get_all_orders(data)
    total_orders = len(all_orders)
    return render_template('dashboard.html', all_orders = all_orders, gross = gross, costs = costs, worked_hours = worked_hours, one_user = one_user ,total_orders = total_orders)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')