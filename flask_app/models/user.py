from flask_app.config.mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from flask import flash

class User:
  def __init__(self, data):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.email = data['email']
    self.password = data['password']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  @classmethod
  def get_all(cls):
    results = connectToMySQL('muro_privado').query_db('SELECT * FROM users;')
    users = []
    for row_user in results:
      users.append(cls(row_user))
    return users

  @staticmethod
  def validate(form):
    is_valid = True

    if len(form['first_name']) < 2:
      flash('First name must be longer than 2 characters', 'register')
      is_valid = False
    if len(form['last_name']) < 2:
      flash('Last name must be longer than 2 characters', 'register')
      is_valid = False
    if not EMAIL_REGEX.match(form['register_email']):
      flash('Invalid email', 'register')
      is_valid = False
    if len(form['register_password']) < 8:
      flash('Password must have at least 8 characters', 'register')
      is_valid = False
    if form['register_password'] != form['confirm_password']:
      flash('Passwords does not match', 'register')
      is_valid = False
    
    query = 'SELECT * FROM users WHERE email = %(register_email)s'
    results = connectToMySQL('muro_privado').query_db(query, form)
    if len(results) >= 1:
      flash('Email already registerd', 'register')
      is_valid = False
    
    return is_valid
  
  @classmethod
  def save(cls, data):
    query = 'INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)'
    newId = connectToMySQL('muro_privado').query_db(query, data)
    return newId
  
  @classmethod
  def get_by_email(cls, data):
    query = 'SELECT * FROM users WHERE email = %(login_email)s'
    result = connectToMySQL('muro_privado').query_db(query, data)
    # no encuentra el email
    if len(result) < 1:
      return False
    else:
      user = cls(result[0])
      return user
  
  @classmethod
  def get_by_id(cls, data):
    query = 'SELECT * FROM users WHERE id = %(id)s'
    result = connectToMySQL('muro_privado').query_db(query, data)
    user = cls(result[0])
    return user