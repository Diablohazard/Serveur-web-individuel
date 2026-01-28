from flask import render_template, request, redirect, url_for
from app import app
users = {}
produits = []

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
    users[username] = password
    print("Utilisateurs :", users)
    return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Affichage de la page (GET)
    if request.method == 'GET':
        return render_template('login.html', produits=produits)

    # Vérification des identifiants (POST)
    username = request.form.get('username')
    password = request.form.get('password')

    if username in users and users[username] == password:
        return render_template('login.html', produits=produits)
    else:
        return "Identifiants incorrects"

@app.route('/produit', methods=['POST'])
def produit():
    nom = request.form.get('produit')
    commentaire = request.form.get('commentaire')

    # Ajouter le produit à la liste
    produits.append({"nom": nom, "commentaire": commentaire})

    return render_template('login.html', produits=produits)