from flask import Flask
from flask import render_template,url_for
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY']='1727idnjiebuydsg982u3ro2unciyg38fbuo3'

class LoginForm(Form):
    username=StringField('username', validators=[InputRequired(),Email(message='fuck your email!')])
    password=PasswordField('password', validators=[InputRequired(),Length(min=5,max=10,message='5 to 10 characters or numbers only')])

@app.route('/', methods=['GET','POST'])
def index():
    form=LoginForm()
    if form.validate_on_submit():
        return 'Form Successfully Submitted!'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
