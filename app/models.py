from app import db

class Blog(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    blog_status = db.Column(db.String(50), nullable=False)
    featured_image_url = db.Column(db.String(255))

    def __repr__(self):
        return f'<Blog {self.title}>'
