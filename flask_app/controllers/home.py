from flask import Flask, render_template, request, redirect, session

from flask_app import app

@app.route('/')
def home():
	return render_template('landing.html')

@app.route('/entrar')
def entrar():
    if 'user_id' in session:
        return redirect('/buscar')
    return render_template('entrar.html')

@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')