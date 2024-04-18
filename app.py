from flask import Flask, render_template, request, redirect, url_for, flash  # Import necessary Flask modules
from forms import RegistrationForm, LoginForm  # Import custom forms from forms.py
from datetime import datetime  # Import datetime module for date handling

app = Flask(__name__)  # Create a Flask app instance
app.config['SECRET_KEY'] = '74fg7628bb0b13ce0c67nf1irn7fb'  # Set a secret key for the app for CSRF protection

# Define a class for blog posts
class BlogPost:
    def __init__(self, author, title, content, date_posted):
        self.author = author
        self.title = title
        self.content = content
        self.date_posted = date_posted

# Sample initial blog posts
posts = [
    BlogPost('Adam Costello', 'Pinned Post_001', 'Welcome to Flask with Friends, a startup blog application allowing you to connect with others easily and effectively, spare no thought and show what your brain has got!', 'March 05, 2024'),
    BlogPost('Adam Costello', 'Pinned Post_002', 'To starting posting, please navigate to to the "Creation" link in the navigation bar above these posts, encourage others to try out Flask with Friends!', 'March 05, 2024')
]

# Route for the home page
@app.route("/")
@app.route("/home")
def home():
    keyword = request.args.get('keyword')  # Get keyword from query parameter
    if keyword:  # If keyword is provided
        # Filter posts based on keyword in title or content
        filtered_posts = [post for post in posts if keyword.lower() in post.title.lower() or keyword.lower() in post.content.lower()]
        return render_template('home.html', posts=filtered_posts, keyword=keyword)  # Render home template with filtered posts
    else:
        return render_template('home.html', posts=posts)  # Render home template with all posts

# Route for the about page
@app.route("/about")
def about():
    return render_template('about.html', title='About')  # Render about template

# Route for creating a new post
@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':  # If form is submitted
        title = request.form['title']  # Get title from form
        content = request.form['content']  # Get content from form
        author = request.form['author']  # Get author from form
        date_posted = datetime.now().strftime("%B %d, %Y")  # Get current date/time
        new_post = BlogPost(author, title, content, date_posted)  # Create a new post object
        posts.append(new_post)  # Add new post to the list of posts
        flash('Post created successfully!', 'success')  # Flash success message
        return redirect(url_for('home'))  # Redirect to home page
    return render_template('create_post.html')  # Render create_post template

# Route for user registration
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()  # Create a registration form instance
    if form.validate_on_submit():  # If form is submitted and validated
        flash(f'Account created for {form.username.data}!', 'success')  # Flash success message
        return redirect(url_for('home'))  # Redirect to home page
    return render_template('register.html', title='Register', form=form)  # Render register template with form

# Route for user login
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()  # Create a login form instance
    if form.validate_on_submit():  # If form is submitted and validated
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':  # Check login credentials
            flash('Login successful, welcome back!', 'success')  # Flash success message
            return redirect(url_for('home'))  # Redirect to home page
        else:
            flash('Login Failed, Please ensure credentials are correct.', 'danger')  # Flash error message
    return render_template('login.html', title='Login', form=form)  # Render login template with form

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode
