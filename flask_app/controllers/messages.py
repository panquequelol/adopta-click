from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.message import Message

@app.route('/send_message', methods=['POST'])
def send_message():
    if 'user_id' not in session:
        return redirect('/')

    #Todos los formularios se reciben con request.form['KEY']
    Message.save(request.form)
    return redirect("/wall")

@app.route('/eliminar/mensaje/<int:id>')
def eliminar(id):
    data = {
        "id": id
    }

    Message.destroy(data)
    return redirect("/wall")