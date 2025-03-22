from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db=SQLAlchemy(app)



class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    content=db.Column(db.Text,nullable=False)

@app.route("/")
@app.route("/home")
def index():
    return render_template('index.html')

@app.route("/create_post",methods=['GET','POST'])
def create_post():
    if request.method == 'POST':
        title=request.form['title']
        content=request.form['content']


        post=Post(title=title,content=content)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('create_post.html')


@app.route("/posts")
def posts():
    posts=Post.query.all()
    return render_template('posts.html',posts=posts)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
