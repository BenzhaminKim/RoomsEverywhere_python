from app import app
from flask import render_template, flash, redirect
from flask import request
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html')

@app.route('/login',methods=['POST','GET'])
def signin():
    form = LoginForm()

    print(request.form)
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data} , {form.remember_me.data}')
        return redirect('/index')

    return render_template('signin.html',form = form)

@app.route('/roomlist',methods=['GET'])
def room_list():
    rooms = [
        {
            'title':'asdasd',
            'price':500
        },
        {
            'title':'wwwww',
            'price':500
        },
    ]
    return render_template('room_list.html',rooms=rooms)