from flask import Flask, render_template, request, redirect, session

from flask_app import app

@app.route('/')
def home():
	return render_template('home.html')

@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')