from flask import Flask, render_template, request, redirect, url_for, flash, jsonify


app = Flask(__name__, template_folder="templates", static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')
    