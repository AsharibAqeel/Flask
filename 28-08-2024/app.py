from flask import Flask , render_template

app = Flask(__name__)

@app.route('/home')
def hello_world():
    return render_template('index.html')

@app.route('/about')
def products():
    name = "Arshoo"
    return render_template('about.html' , name = name )

if __name__ == '__main__':
    app.run(debug=True)