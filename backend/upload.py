from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app
)

import os

from werkzeug.exceptions import abort

UPLOAD_FOLDER = "../instance/images"
ALLOWED_EXTENSIONS = {'png', 'jpeg'}

bp = Blueprint('upload', __name__)

@bp.route('/upload', methods=['POST'])
def upload():
    try:
        image = request.files.get('image', '')
        print(request.files)
        print(image)
        if image is not None:
            print("image recieved!")
        filename = "test blob"
        createImageFolder(UPLOAD_FOLDER)
        current_app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
        return "image uploaded"
    except Exception as err:
        abort(err)
     


#Create image folder and throw error if unable to
def createImageFolder(path):
    try:
        os.makedirs(path, exist_ok = True)
        print ("image directory made!")
    except OSError as error:
        print ("image directory could not be made")

#Check if file is a valid file type
def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

# createImageFolder()
