from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Pet:
  def __init__(self, data):
    self.id = data['id']
    self.name = data['name']
    self.type = data['type']
    self.age = data['age']
    self.location = data['location']
    self.description = data['description']
    self.phone = data['phone']
    self.image = data['image']
    self.gender = data['gender']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.user_id = data['user_id']
  
  @classmethod
  def get_all(cls):
    results = connectToMySQL('adoptaclick').query_db('SELECT * FROM pets;')
    pets = []
    for row in results:
      pets.append(cls(row))
    return pets
  
  @classmethod
  def save(cls, data):
    query = 'INSERT INTO pets (name, type, age, location, description, phone, image, user_id, gender) VALUES (%(name)s, %(type)s, %(age)s, %(location)s, %(description)s, %(phone)s, %(image)s, %(user_id)s, %(gender)s)'
    newId = connectToMySQL('adoptaclick').query_db(query, data)
    return newId

  @classmethod
  def get_by_id(cls, data):
    query = 'SELECT * FROM pets WHERE id = %(id)s'
    result = connectToMySQL('adoptaclick').query_db(query, data)
    pet = cls(result[0])
    return pet

  @classmethod
  def get_all_by_user_id(cls, data):
    query = 'SELECT * FROM pets WHERE user_id = %(user_id)s'
    results = connectToMySQL('adoptaclick').query_db(query, data)
    pets = []
    for row in results:
      pets.append(cls(row))
    return pets
  
  @classmethod
  def get_filtered(cls, data):
    query = 'SELECT * FROM pets WHERE location = %(location)s and type = %(type)s'
    results = connectToMySQL('adoptaclick').query_db(query, data)
    pets = []
    print('👉', data, results)
    for row in results:
      pets.append(cls(row))
    return pets

  @classmethod
  def destroy(cls, data):
    query = 'DELETE FROM pets WHERE (id = %(id)s);'
    result = connectToMySQL('adoptaclick').query_db(query, data)
    return result
  
  @classmethod
  def update(cls, data):
    query = 'UPDATE pets SET name = %(name)s, type = %(type)s, age = %(age)s, location = %(location)s, description = %(description)s, phone = %(phone)s, image = %(image)s, gender = %(gender)s WHERE (id = %(id)s);'
    result = connectToMySQL('adoptaclick').query_db(query, data)
    return result

  @staticmethod
  def validate(form):
    is_valid = True
    if len(form['name']) < 2:
      flash('El nombre debe contener al menos 2 caracteres', 'pet')
      is_valid = False
    if form['age'] == '':
      flash('Debes ingresar una edad', 'pet')
      is_valid = False
    if len(form['phone']) < 8:
      flash('Debes ingresar un número de teléfono personal apropiado', 'pet')
      is_valid = False
    if form['description'] == '':
      flash('Debes contarnos al menos un poco de la mascota en la descripcion', 'pet')
      is_valid = False
    # ! VALIDAR IMAGEN
    return is_valid