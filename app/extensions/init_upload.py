from flask import Flask
from flask_uploads import UploadSet, IMAGES, configure_uploads
from werkzeug.utils import secure_filename

photo = UploadSet('photos', IMAGES)


def initialize_upload(app: Flask):
    configure_uploads(app, photo)
