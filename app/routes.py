from flask import render_template, request, redirect, url_for
from app import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/inscription')
def inscription():
    return render_template('inscription.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    # Ici, tu pourrais enregistrer les identifiants dans une base de données ou un fichier
    # Exemple : print(username, password) pour debug
    print(f"Nouvel utilisateur : {username}, mot de passe : {password}")
    return redirect(url_for('home'))

@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    return render_template('login.html', username=username, password=password)