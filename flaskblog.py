from flask import Flask
from flask import render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Ajay Shah',
        'title': 'Blog post 1',
        'content': 'First Post Content',
        'date_posted': 'Dec 14, 2021'
    },

    {
        'author': 'Manish Sah',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'Dec 15, 2021'
    }

]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)


