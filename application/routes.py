from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user, current_user

from application import app
from application.model import *
from application.form import *
from application.utils import save_image

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()
        if user and password == user.password:
            login_user(user)
            return redirect(url_for('index', username=username))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html', title="Login", form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditProfileForm()

    if form.validate_on_submit():
        user = User.query.get(current_user.id)
        if form.username.data != user.username:
            user.username = form.username.data
        user.fullname = form.fullname.data
        user.bio = form.bio.data

        if form.profile_pic.data:
            pass
            
        db.session.commit()
        flash('Profile Updated.', 'success')
        return redirect(url_for('profile', username=current_user.username))

    form.username.data = current_user.username
    form.fullname.data = current_user.fullname
    form.bio.data = current_user.bio

    return render_template('editProfile.html', title=f'Edit {current_user.username}s Profile', form=form)

@app.route('/<string:username>')
@login_required
def profile(username):

    posts = current_user.posts
    return render_template('profile.html', title=f'{current_user.fullname} Profile', posts=posts)


@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = CreatePostForm()

    if form.validate_on_submit():
        post = Post(
            author_id = current_user.id,
            caption = form.caption.data
        )
        post.photo = save_image(form.post_pic.data)
        db.session.add(post)
        db.session.commit()
        flash('Your image has been posted', 'success')

    # page = request.args.get('page', 1, type=int)
    # posts = Post.query.filter_by(author_id = current_user.id).order_by(Post.post_date.desc()).paginate(page=page, per_page=3)

    # without paginate (pages)
    posts = current_user.posts

    return render_template('index.html', title='Home', form=form, posts=posts)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        username = form.username.data
        fullname = form.fullname.data
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()
        if user:
            flash('That username is already taken. Please choose a different one.', 'error')
        else:
            new_user = User(username=username, password=password, fullname=fullname, email=email)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created', 'success')
            return redirect(url_for('login'))
   
    return render_template('signup.html', title='SignUp', form=form)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/createPost')
@login_required
def create():
    form = CreatePostForm()

    if form.validate_on_submit():
        post = Post(
            author_id = current_user.id,
            caption = form.caption.data
        )
        post.photo = save_image(form.post_pic.data)
        db.session.add(post)
        db.session.commit()
        flash('Your image has been posted', 'success')
    posts = current_user.posts

    return render_template('index.html', title='Home', form=form, posts=posts)


if __name__ == '__main__':
    app.run(debug=True)