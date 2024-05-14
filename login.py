from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

#creating a dummy database
users = {"augusten":"RabiRabi", "Rabi":"Rabi@2020"}

@app.route('/')
def home():
    return render_template("login.html")

@app.route('/login', methods=['POST'])

def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('home', showerror='invalid username or password!'))
    
@app.route('/dashboard')
def dashboard():
    return "welcome to the dashboard"
if __name__ == '__main__':
    app.run(debug=True)