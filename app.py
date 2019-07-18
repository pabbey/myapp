from flask import Flask
from flask import render_template
from wtforms import Form, BooleanField, StringField, PasswordField, validators
app = Flask(__name__)



class RegistrationForm():
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])


@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(login.form)
    if login.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('login.html', form=form)
@app.route('/')
def index():
    return render_template('main.html')
if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0', port='5009')
    
    


