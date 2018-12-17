from flask import Flask, render_template

app = Flask(__name__)



@app.route('/temp')
def hello_world():
    return render_template('/index.md')

@app.route('/')
def source_sep():
    return render_template('/source_sep.html')

if __name__ == '__main__':
    app.run('0.0.0.0')
