
# TODO: todo sobre manipular la tabla users de la base de datos users_schema va aqui, se trabaja con POO
# from flask_app.config.mysqlconnection import connectToMySQL

# class User:
#   def __init__(self, data):
#     self.id = data['id']
#     self.first_name = data['first_name']
#     self.last_name = data['last_name']
#     self.email = data['email']
#     self.created_at = data['created_at']
#     self.updated_at = data['updated_at']

# ! users_schema es el nombre de la base de datos
#   @classmethod
#   def get_all(cls):
#     results = connectToMySQL('users_schema').query_db('SELECT * FROM users;')
#     users = []
#     for row_user in results:
#       users.append(cls(row_user))
#     return users

#   @classmethod
#   def delete(cls, data):
#     query = "DELETE FROM users WHERE id = %(id)s;"
#     result = connectToMySQL('users_schema').query_db(query, data)
#     return result
