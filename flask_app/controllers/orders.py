from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models import order, service, user

@app.route('/new_order')
def new_order():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id' : session['user_id']
    }
    one_user = user.User.one_user_info(data)
    all_services = service.Service.all_user_services(data)
    return render_template('new_order.html', all_services = all_services, one_user = one_user)

@app.route('/create_order', methods=['POST'])
def create_order():
    if 'user_id' not in session:
        return redirect('/')
    if not order.Order.validate_order(request.form):
        return redirect('/new_order')
    data = {
        'customer_name' : request.form['customer_name'],
        'date' : request.form['date'],
        'notes' : request.form['notes'],
        'service_id' : request.form['service_id'],
        'business_id' : request.form['business_id']
    }
    print("data")
    print(data)
    order.Order.save(data)
    return redirect(f"/dashboard/{session['user_id']}")

@app.route('/show_order/<int:id>')
def show_order(id):
    if 'user_id' not in session:
        return ('/')
    data = {
        'id' : id
    }
    one_order = order.Order.get_one_order(data)
    return render_template('show_order.html', one_order = one_order)

@app.route('/edit_order/<int:id>')
def edit_order(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id' : id
    }
    serve = {
        'id': session['user_id']
    }
    all_services = service.Service.all_user_services(serve)
    one_order = order.Order.get_one_order(data)
    print(one_order)
    return render_template('edit_order.html', one_order = one_order, all_services = all_services)

@app.route('/update_order/<int:id>', methods=['POST'])
def update_order(id):
    if 'user_id' not in session:
        return ('/')
    data = {
        'id' : request.form['id'],
        'customer_name' : request.form['customer_name'],
        'service_id' : request.form['service_id'],
        'date' : request.form['date'],
        'notes' : request.form['notes']
    }
    order.Order.update_order(data)
    return redirect(f"/dashboard/{session['user_id']}")

@app.route('/delete_order/<int:id>')
def delete_order(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id' : id
    }
    order.Order.delete_order(data)
    return redirect(f"/dashboard/{session['user_id']}")