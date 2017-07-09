from flask import Flask
from flask import render_template,url_for

app = Flask(__name__)
app.config['SECRET_KEY']='1727idnjiebuydsg982u3ro2unciyg38fbuo3'


@app.route('/', methods=['GET','POST'])
def index():   
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
