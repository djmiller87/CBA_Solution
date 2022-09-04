from flask_app import app
from flask import redirect, render_template, session, request, flash
from flask_app.models import service, user

@app.route('/services')
def all_services():
    if not 'user_id' in session:
        return redirect('/')
    data = {
        'id' : session['user_id']

    }
    all_services = service.Service.all_user_services(data)
    one_user = user.User.one_user_info(data)
    return render_template('services.html', one_user = one_user, all_services = all_services)

@app.route('/new_service')
def new_service():
    if not 'user_id' in session:
        return redirect('/')
    data = {
        'id' : session['user_id']
    }
    one_user = user.User.one_user_info(data)
    return render_template('/new_service.html', one_user = one_user)


@app.route('/create_service', methods=['POST'])
def create_service():
    if 'user_id' not in session:
        return redirect('/')
    if not service.Service.validate_service(request.form):
        return redirect('/new_service')
    data = {
        'service_name': request.form['service_name'],
        'hours': request.form['hours'],
        'price': request.form['price'],
        'business_cost': request.form['business_cost'],
        'description': request.form['description'],
        'user_id': request.form['user_id']
    }
    service.Service.save(data)
    return redirect(f"/dashboard/{session['user_id']}")

@app.route('/edit_service/<int:id>')
def edit_service(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id' : session['user_id']
    }
    a_service = {
        'id' : id
    }
    # print(a_service)
    one_user = user.User.one_user_info(data)
    one_service = service.Service.get_one_service(a_service)
    return render_template('edit_service.html', one_service = one_service, one_user = one_user)

@app.route('/update_service/<int:id>', methods=['POST'])
def update_service(id):
    if 'user_id' not in session:
        return redirect('/')
    if not service.Service.validate_service(request.form):
        return redirect(f"/edit_service/{id}")
    data = {
        'id': id,
        'service_name': request.form['service_name'],
        'hours': request.form['hours'],
        'price': request.form['price'],
        'business_cost': request.form['business_cost'],
        'description': request.form['description']
    }
    service.Service.update_service(data)
    return redirect(f"/dashboard/{session['user_id']}")

@app.route('/show_service/<int:id>')
def show_service(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id' : session['user_id']
    }
    a_service = {
        'id' : id
    }
    one_user = user.User.one_user_info(data)
    one_service = service.Service.get_one_service(a_service)
    return render_template('show_service.html', one_service = one_service, one_user = one_user )

@app.route('/delete/<int:id>')
def delete(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id' : id
    }
    service.Service.delete_service(data)
    return redirect(f"/dashboard/{session['user_id']}")
