from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import os  # For file path manipulation

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './'

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'document_attachment_doc' not in request.files:
            return redirect(request.url)  # Redirect to same page if no file

        file = request.files['document_attachment_doc']

        # Validate allowed file extensions (optional)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            # Handle successful upload (e.g., display success message)
            return 'File uploaded successfully!'
        else:
            # Handle invalid file type (e.g., display error message)
            return 'Invalid file type!'

    # Render the form on GET request
    return render_template('images.html')