from flask import Flask, render_template, request, redirect, session, flash

from flask_app import app
from flask_app.models.user import User
from flask_app.models.pet import Pet

from werkzeug.utils import secure_filename
import os

@app.route('/buscar')
def buscar_mascota():
  if 'user_id' not in session:
    return redirect('/entrar')

  data = {
    'id': session['user_id']
  }
  user = User.get_by_id(data)

  if 'pets' not in globals():
    pets = Pet.get_all()

  return render_template('buscar.html', user = user, pets = pets)

@app.route('/buscar/filtrar', methods=['POST'])
def buscar_filtrados():
  if 'user_id' not in session:
    return redirect('/entrar')
  
  data = {
    'location': request.form['location'],
    'type': request.form['type']
  }

  user = User.get_by_id({'id': session['user_id']})

  pets = Pet.get_filtered(data)
  return render_template('buscar.html', user = user, pets = pets)

@app.route('/buscar/add')
def add_mascota():
  if 'user_id' not in session:
    return redirect('/entrar')

  return render_template('nueva_mascota.html', user_id = session['user_id'])

@app.route('/buscar/create', methods=['POST'])
def create_mascota():
  if 'user_id' not in session:
    return redirect('/entrar')

  if Pet.validate(request.form) == False:
    return redirect('/buscar/add')

  # Validaciones de la imagen
  if 'image' not in request.files:
    flash('Imagen no encontrada', 'pets')
    return redirect('/buscar/add')

  image = request.files['image']
  
  if image.filename == '':
    flash('Nombre de imagen vacío', 'pets')
    return redirect('/buscar/add')

  nombre_imagen = secure_filename(image.filename)
  image.save(os.path.join(app.config['UPLOAD_FOLDER'], nombre_imagen))

  formulario = {
    'name': request.form['name'],
    'description': request.form['description'],
    'type': request.form['type'],
    'age': request.form['age'],
    'location': request.form['location'],
    'phone': request.form['phone'],
    'gender': request.form['gender'],
    'user_id': request.form['user_id'],
    'image': nombre_imagen
  }

  Pet.save(formulario)
  return redirect('/buscar')

@app.route('/destroy/<id>')
def destroy(id):
  if 'user_id' not in session:
    return redirect('/entrar')

  Pet.destroy({ 'id': id })
  return redirect('/publicaciones')

@app.route('/edit/<id>')
def edit(id):
  if 'user_id' not in session:
    return redirect('entrar')
  pet = Pet.get_by_id({ 'id': id })

  return render_template('editar_mascota.html', pet = pet, user_id = session['user_id'])

@app.route('/update', methods=['POST'])
def update_pet():
  if 'user_id' not in session:
    return redirect('/entrar')
  
  if Pet.validate(request.form) == False:
    return redirect('/buscar/add')

  # Validaciones de la imagen
  if 'image' not in request.files:
    flash('Imagen no encontrada', 'pets')
    return redirect('/buscar/add')

  image = request.files['image']
  
  if image.filename == '':
    flash('Nombre de imagen vacío', 'pets')
    return redirect('/buscar/add')

  nombre_imagen = secure_filename(image.filename)
  image.save(os.path.join(app.config['UPLOAD_FOLDER'], nombre_imagen))

  formulario = {
    'id': request.form['id'],
    'name': request.form['name'],
    'description': request.form['description'],
    'type': request.form['type'],
    'age': request.form['age'],
    'location': request.form['location'],
    'phone': request.form['phone'],
    'gender': request.form['gender'],
    'user_id': request.form['user_id'],
    'image': nombre_imagen
  }

  Pet.update(formulario)
  return redirect('/buscar')

@app.route('/publicaciones')
def gestionar_publicaciones():
  if 'user_id' not in session:
    return redirect('/entrar')
  data = {
    'id': session['user_id']
  }
  user = User.get_by_id(data)
  pets = Pet.get_all_by_user_id({'user_id':session['user_id']})
  return render_template('gestionar_publicaciones.html', user = user, pets = pets)

@app.route('/mostrar')
def mostrar_mascota():
  return render_template('mostrar_mascota.html')
