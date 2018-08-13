from flask import Flask, render_template, request, session, url_for, redirect
from wtforms import ValidationError

from models import db, User
from forms import SignUpForm, LoginForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask'
db.init_app(app)

app.secret_key = "le@rning#flask"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if 'email' in session:
        return redirect(url_for('home'))
    form = SignUpForm()
    if form.validate_on_submit():
        new_user = User(form.first_name.data, form.last_name.data, form.email.data, form.pwd.data)
        db.session.add(new_user)
        db.session.commit()
        # Create a new session
        session['email'] = new_user.email
        return redirect(url_for('home'))
    else:
        return render_template('signup.html', form=form)

@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'email' not in session:
        return render_template('index.html')

    return render_template('home.html')

@app.route('/signin', methods=['GET', 'POST'])
def login():
    if 'email' in session:
        return redirect(url_for('home'))
    form = LoginForm()
    # validate_on_submit() checks if the request is POST, PATCH, PUT or DELETE and valida form
    # So dont have to check seperately if request is GET or POST
    if form.validate_on_submit():
        print('Form validated')
        email = form.email.data
        pwd = form.pwd.data
        user = User.query.filter_by(email=email).first()
        print(user)
        if user is not None and user.check_password(pwd):
            print('user found')
            session['email'] = user.email
            return render_template('home.html')
        else:
            # Try to see if it can be done by custom validator. See the case will it still try to find an user even when the email is empty
            if not user:
                form.email.errors.append('We could not find the email id in our registered users')
            else:
                form.pwd.errors.append('Please enter correct password')
            return render_template('signin.html', form=form)
    else:
        return render_template('signin.html', form=form)

@app.route('/signout')
def logout():
    session.pop('email',None)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
