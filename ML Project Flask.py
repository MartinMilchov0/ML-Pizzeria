from flask import Flask, render_template, redirect
from flask import request
from flask import Flask, url_for, request, redirect

app = Flask(__name__, template_folder= 'templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template("homepage/menu.html")

@app.route('/aboutus')
def about():
    return render_template("homepage/about.html")

@app.route('/offers')
def offers():
    return render_template("offers.html")

@app.route('/order')
def order():
    return render_template("order.html")

#if the login is succesful it redirects to index.html, this will be changed to redirect to pmanager.html
@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        admin_name = "Ivancho"
        admin_password = "1234"

        username = request.form['username']
        password = request.form['password']

        if username == admin_name and password == admin_password:
            return redirect('/')

    return render_template('login.html')

if __name__=='__main__':
    app.run(debug=True)

#pmanager.html is a page meant for the chef/cashier
@app.route('/pizzamanger')
def pizza_manager():
    return render_template("pmanager.html")

app.debug = True