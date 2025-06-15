from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('user')
    pw = request.form.get('password')
    # Tidak memeriksa password sama sekali!
    resp = make_response(redirect('/flag'))
    resp.set_cookie('username', user or '')
    resp.set_cookie('password', pw or '')
    resp.set_cookie('admin', 'False')
    return resp

@app.route('/flag')
def flag():
    admin = request.cookies.get('admin', 'False')
    if admin == 'True':
        return render_template('flag.html')
    return "<h3>Access Denied. You are not admin.</h3>", 403

@app.route('/logout')
def logout():
    resp = make_response(redirect('/'))
    resp.set_cookie('username', '', expires=0)
    resp.set_cookie('password', '', expires=0)
    resp.set_cookie('admin', '', expires=0)
    return resp

if __name__ == '__main__':
    app.run(debug=True)
