from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '76d5f16cf6bb57be0bd6851a8c61df1d'  # secret key for security
posts = [
    {
        'author': 'corey taylor',
        'band': 'slipknot',
        'content': 'nu metal',
        'date': 'april'
    },
    {
        'author': 'taylor momsen',
        'band': 'pretty reckless',
        'content': 'metal',
        'date': 'june'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts, title='itworks')  # we have access to post in the template


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login done!', 'success')
        return redirect(url_for('home'))
    return render_template("login.html", title='Login', form=form)


if __name__ == '__main__':
    app.run()
