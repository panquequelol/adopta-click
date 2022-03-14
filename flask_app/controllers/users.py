
# ! Ejemplo con users
# TODO: hacer rutas relacionadas a users

# from flask import Flask, render_template, request, redirect, session

# from flask_app import app
# from flask_app.models.users import User


# @app.route('/')
# def home():
# 	return redirect('/users')

# @app.route('/users')
# def dashboard():
# 	return render_template('dashboard.html', users=User.get_all())

# @app.route('/users/<id>/destroy')
# def delete(id):
# 	data = {'id': id} # la informacion necesita ser pasada como diccionario
# 	User.delete(data)
# 	return redirect('/users')