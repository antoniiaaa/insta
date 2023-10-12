from application import db
from datetime import DateTime

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    fullname = db.Column(db.String(128), nullable=False)
    bio = db.Column(db.String(256))
    image = db.Column(db.String(256), nullable=False, default="squids.png")
    join_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Boolean, default=True)

class Relation(db.Model):
    __tablename__ = "relation"
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    following_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    status = db.Column(db.Boolean, default=True)
    relation_date = db.Column(db.DateTime, default=datetime.utcnow)

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(256), default="")
    image = db.Column(db.String(128), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    status = db.Column(db.Boolean, default=True)

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("post_id"), nullable=False)
    commenter_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    text = db.Column(db.Text, nullable=True)
    comment_date = db.Column(db.DateTime, default=datetime.utcnow)
    hidden = db.Column(db.Boolean, default=False)

class Like(db.Model):
    __tablename__ = "likes"
    id = db.Column(db.Integer, primary_key=True)
    user_id = = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post_id"), nullable=False)
    status = db.Column(db.Boolean, default=True)
    like_date = db.Column(db.DateTime, default=datetime.utcnow)