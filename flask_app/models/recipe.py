from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Recipe:
  def __init__(self, data):
    self.id = data['id']
    self.name = data['name']
    self.instructions = data['instructions']
    self.description = data['description']
    self.under_30 = data['under_30']
    self.date_made = data['date_made']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.user_id = data['user_id']
  
  @classmethod
  def get_all(cls):
    results = connectToMySQL('recipe_db').query_db('SELECT * FROM recipes;')
    recipes = []
    for row in results:
      recipes.append(cls(row))
    return recipes
  
  @classmethod
  def save(cls, data):
    query = 'INSERT INTO recipes (name, under_30, description, instructions, date_made, user_id) VALUES (%(name)s, %(under_30)s, %(description)s, %(instructions)s, %(date_made)s, %(user_id)s)'
    newId = connectToMySQL('recipe_db').query_db(query, data)
    return newId

  @classmethod
  def get_by_id(cls, data):
    query = 'SELECT * FROM recipes WHERE id = %(id)s'
    result = connectToMySQL('recipe_db').query_db(query, data)
    recipe = cls(result[0])
    return recipe

  @classmethod
  def destroy(cls, data):
    query = 'DELETE FROM recipes WHERE (id = %(id)s);'
    result = connectToMySQL('recipe_db').query_db(query, data)
    return result
  
  @classmethod
  def update(cls, data):
    query = 'UPDATE recipes SET name = %(name)s, under_30 = %(under_30)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s WHERE (id = %(id)s);'
    result = connectToMySQL('recipe_db').query_db(query, data)
    return result


  @staticmethod
  def validate(form):
    is_valid = True
    if len(form['name']) < 3:
      flash("Name must be at least 3 characters long", 'recipe')
      is_valid = False
    if len(form['description']) < 3:
      flash('Description must be at least 3 characters long', 'recipe')
      is_valid = False
    if len(form['instructions']) < 3:
      flash('Instructions must be at least 3 characters long', 'recipe')
      is_valid = False
    if form['date_made'] == '':
      flash('You must enter a date', 'recipe')