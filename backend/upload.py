from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app
)
import os
from werkzeug.utils import secure_filename
from werkzeug.exceptions import abort

UPLOAD_FOLDER = ""
ALLOWED_EXTENSIONS = {'png', 'jpeg'}

bp = Blueprint('upload', __name__)

@bp.route('/upload', methods=['POST'])
def upload():
    try:
        if 'image' not in request.files:
            print('No image part')
            return
        # Get image file and store it
        image = request.files.get('image', '')

        print(image)
        filename = secure_filename(image.filename) + ".png"
        # Change UPLOAD_FOLDER value in function in order to avoid startup errors
        UPLOAD_FOLDER = current_app.instance_path
        createImageFolder(UPLOAD_FOLDER)
        current_app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
        print((os.path.join(current_app.config['UPLOAD_FOLDER'])), " upload path")

        image.save(os.path.join(current_app.config['UPLOAD_FOLDER'], "images", filename))
        return "'"
    except Exception as err:
        abort(err)
     


#Create image folder and throw error if unable to
def createImageFolder(path):
    try:
        os.makedirs(path + "/images", exist_ok = True)
        print ("image directory made!")
    except OSError as error:
        print ("image directory could not be made")

#Check if file is a valid file type
def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

# createImageFolder()
