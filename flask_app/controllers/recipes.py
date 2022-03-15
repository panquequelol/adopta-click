from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/dashboard')
def recipes():
  if 'user_id' not in session:
    redirect('/')
  data = {
    'id': session['user_id']
  }
  user = User.get_by_id(data)
  recipes = Recipe.get_all()
  user_in_session = session['user_id']
  return render_template('dashboard.html', user = user, recipes = recipes,user_in_session = user_in_session)

@app.route('/recipes/new')
def new_recipe():
  if 'user_id' not in session:
    return redirect('/')
  return render_template('new_recipe.html', user_id = session['user_id'])

@app.route('/recipes/create', methods=['POST'])
def create_recipe():
  if Recipe.validate(request.form) == False:
    return redirect('/recipes/new')
  Recipe.save(request.form)
  return redirect('/dashboard')

@app.route('/recipe/<id>')
def show_recipe(id):
  if 'user_id' not in session:
    return redirect('/')
  data = {
    'id': id
  }
  recipe = Recipe.get_by_id(data)
  return render_template('show_recipe.html', recipe = recipe)

@app.route('/destroy/<id>')
def destroy_recipe(id):
  if 'user_id' not in session:
    return redirect('/')
  data = {
    'id': id
  }
  Recipe.destroy(data)
  return redirect('/dashboard')

@app.route('/edit/<id>')
def edit_recipe(id):
  if 'user_id' not in session:
    return redirect('/')
  data = {
    'id': id
  }
  recipe = Recipe.get_by_id(data)
  user_id = session['user_id']
  return render_template('edit_recipe.html', recipe = recipe, user_id = user_id)

@app.route('/recipes/update', methods=['POST'])
def update():
  if 'user_id' not in session:
    return redirect('/')
  data = {
    'id': request.form['id']
  }
  recipe = Recipe.get_by_id(data)
  Recipe.update(request.form)
  return redirect('/dashboard')
