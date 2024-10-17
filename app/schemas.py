from app import ma
from app.models import Blog

class BlogSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Blog
      # load_instance = True

# Instancia del esquema
blog_schema = BlogSchema()
blogs_schema = BlogSchema(many=True)