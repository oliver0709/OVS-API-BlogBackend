from app import create_app, db
from app.models import Blog

# Crea una instancia de la aplicación
app = create_app()

# Crear un contexto de aplicación
with app.app_context():
    # Función para actualizar las URLs de las imágenes
    def update_blog_image_urls():
        blogs = Blog.query.all()
        
        for blog in blogs:
            if blog.featured_image_url:
                # Imprimimos la URL original para depuración
                print(f"Original: {blog.featured_image_url}")

                # Verificamos si la URL ya contiene 'uploads/' y lo removemos si es necesario
                if 'uploads/' in blog.featured_image_url:
                    
                    filename = blog.featured_image_url.split('uploads/')[-1]  
                    
                    blog.featured_image_url = f'http://localhost:5000/static/uploads/{filename}'
                else:
                    # Si no hay 'uploads/' en la URL, simplemente la formateamos correctamente
                    filename = blog.featured_image_url.split('/')[-1]  
                    blog.featured_image_url = f'http://localhost:5000/static/uploads/{filename}'
                
                
                db.session.commit()

                # Imprimimos la URL actualizada para depuración
                print(f"Actualizada: {blog.featured_image_url}")

        print("Todas las URLs de las imágenes han sido actualizadas.")

    update_blog_image_urls()
