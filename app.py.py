from flask import Flask, render_template, request, redirect

app = Flask(__name__)

#login username and login password
valid_users = {'admin': 'admin'}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if valid_users.get(username) == password:
        return "Login successful!"
    else:
        return "Invalid credentials. Please try again."

if __name__ == '__main__':
    app.run(debug=True)
