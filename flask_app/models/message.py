from flask_app.config.mysqlconnection import connectToMySQL
import re

from flask import flash

class Message:
  def __init__(self, data):
    self.id = data['id']
    self.content = data['content']
    self.receiver_id = data['receiver_id']
    self.sender_id = data['sender_id']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

    self.sender = data["sender"]
    self.receiver = data["receiver"]

  @classmethod
  def save(cls, form):
    query = 'INSERT INTO messages (content, sender_id, receiver_id) VALUES (%(content)s, %(sender_id)s, %(receiver_id)s);'
    return connectToMySQL('muro_privado').query_db(query, form)
  
  @classmethod
  def get_user_messages(cls, data):
    query = "SELECT messages.*, senders.first_name as sender, receivers.first_name as receiver FROM messages LEFT JOIN users as senders ON senders.id = sender_id LEFT JOIN users as receivers ON receivers.id = receiver_id WHERE receiver_id = %(id)s;"
    results = connectToMySQL('muro_privado').query_db(query, data)
    messages = []
    for message in results:
        messages.append(cls(message))
    return messages
  
  @classmethod
  def destroy(cls, data):
    query = "DELETE FROM messages WHERE (id = %(id)s);"
    result = connectToMySQL('muro_privado').query_db(query, data)
    return result