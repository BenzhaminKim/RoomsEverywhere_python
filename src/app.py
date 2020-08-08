from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    rooms = [{"title":"The cheapest room","price":500},
            {"title":"The cheapest ever room","price":700},
            {"title":"The cheapest dulex room","price":800}]

    return render_template('index.html',rooms = rooms)

@app.route('/signin',methods=['GET','POST'])
def signin():
    if request.method == "POST":
        print(request.form)
        print(request.get_json)

    return render_template('signin.html')
    
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')