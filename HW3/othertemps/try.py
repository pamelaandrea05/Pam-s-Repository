from flask import Flask , redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/register')
def register():
    dept=request.form.getlist('dept')
    return render_template('registet.html')

@app.route('/data', methods=['POST', 'GET']) 
def data():
    if request.method == 'POST':
        dept=request.form.getlist('dept')
        num=request.form['num'] 
        return render_template('registet.html', dept=dept)

@app.route('/login')
def process():
    return render_template('index.html')

# @app.route('/process', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         pang=request.form['name']
#     elif request.method == 'GET':
#         pang=request.args.get('name')
#         return f"<h1>Hello <i>{pang}</i></h1>"

# @app.route('/process', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         pang=request.form['name']
#     elif request.method == 'GET':
#         pang=request.args.get('name')
#         return render_template('result.html', name=pang)
    
@app.route('/process', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        pang=request.form['name']
    elif request.method == 'GET':
        pang=request.args.get('name')
    dict={'id':101, 'name':pang, 'age':21}
    return render_template('result.html', student=dict)
    
@app.route('/<user>')
def server(user):
    if user == 'Cariaga':
        return redirect(url_for('admin', name=user))
    else:
        return redirect(url_for('guest', name=user))
    
@app.route('/admin/<name>')
def admin(name):
    return f"<h1> Hello Admin <i>{name}</i> </h1>"

@app.route('/guest/<name>')
def guest(name):
    return f"<h1> Hello Guest <i>{name}</i> </h1>"

@app.route('/')
def home():
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    return f"<h1>This is the profile</h1>"

@app.route('/profile/')
def prof():
    return f"<h1>This is another profile</h1>"

@app.route('/<name>/<sex>/<address>')
def welcome(name, sex, address):
    return f"<h1>Hello PSU <i>{name}</i> {sex} <i>{address}</i></h1>"

if __name__ == '__main__':
    app.run(debug=True)
