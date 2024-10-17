import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads'

def save_test_file():
    # Simula un archivo subido
    class File:
        filename = 'test_image.jpg'
        def save(self, path):
            with open(path, 'w') as f:
                f.write('test content')

    file = File()
    if file.filename:
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        print(f"Saving file to: {file_path}")
        file.save(file_path)
        print(f"File saved: {file_path}")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
save_test_file()
