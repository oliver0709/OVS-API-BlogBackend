from flask import request, jsonify, Blueprint, send_from_directory, url_for  
from app import db
from app.models import Blog
from app.schemas import blog_schema, blogs_schema
from flask_jwt_extended import jwt_required
import os
from werkzeug.utils import secure_filename


# Directorio donde se almacenarán las imágenes
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Blueprint para el manejo de blogs
blog_bp = Blueprint('blog_bp', __name__)

# GET para obtener todos los blogs
@blog_bp.route('/portfolio_blogs', methods=['GET'])
def get_blogs():
    blogs = Blog.query.all()
    return jsonify({
        "portfolio_blogs": blogs_schema.dump(blogs),
        "meta": {
            "total_pages": 1,
            "total_records": len(blogs)
        }
    })

# GET para obtener un blog específico
@blog_bp.route('/portfolio_blogs/<int:id>', methods=['GET'])
def get_blog(id):
    blog = Blog.query.get_or_404(id)
    return blog_schema.jsonify(blog)

# POST para crear un blog
@blog_bp.route('/portfolio_blogs', methods=['POST'])
@jwt_required()

def create_blog():
    try:
        title = request.form['title']
        content = request.form['content']
        blog_status = request.form['blog_status']

        featured_image_url = None

        # Verificar si hay una imagen en los archivos
        if 'featured_image' not in request.files:
            print("No featured_image key in request.files")
        else:
            file = request.files['featured_image']
            if file.filename == '':
                print("No file selected")
            elif file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(UPLOAD_FOLDER, filename)
                print(f"File path: {file_path}")  # Depuración
                file.save(file_path)
                print(f"File saved: {file_path}")  # Depuración
                featured_image_url = url_for('static', filename=f'uploads/{filename}', _external=True)
                print(f"File URL: {featured_image_url}")  # Depuración

        new_blog = Blog(
            title=title,
            content=content,
            blog_status=blog_status,
            featured_image_url=featured_image_url
        )
        db.session.add(new_blog)
        db.session.commit()
        return blog_schema.jsonify(new_blog), 201

    except KeyError as e:
        return jsonify({"error": f"Missing key: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# PATCH para actualizar un blog
@blog_bp.route('/portfolio_blogs/<int:id>', methods=['PATCH'])
@jwt_required()
def update_blog(id):
    blog = Blog.query.get_or_404(id)

    blog.title = request.form.get('title', blog.title)
    blog.content = request.form.get('content', blog.content)
    blog.blog_status = request.form.get('blog_status', blog.blog_status)

    # Actualizar imagen si hay una nueva subida
    if 'featured_image' in request.files:
        file = request.files['featured_image']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            blog.featured_image_url = url_for('static', filename=f'uploads/{filename}', _external=True)

    db.session.commit()

    return blog_schema.jsonify(blog)

# DELETE para eliminar un blog
@blog_bp.route('/portfolio_blogs/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_blog(id):
    blog = Blog.query.get_or_404(id)

    db.session.delete(blog)
    db.session.commit()

    return jsonify({'message': 'Blog deleted successfully'}), 200
