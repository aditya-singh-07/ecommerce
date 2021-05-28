import os
import pathlib

from flask import Blueprint, redirect, render_template, request, url_for, flash, Flask, jsonify, Response, make_response
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from .model_admin import db
from ecommerce.model_admin import Apparels

app = Flask(__name__)

UPLOAD_FOLDER = './ecommerce/static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

admin = Blueprint('admin', __name__)

@admin.route('/admin')
def dashboard():
    return render_template('admin/index.html')

@admin.route('/admin/products')
def view_products():
    page_global = request.args.get('page', 1, type=int)
    apparel_data = Apparels.query.paginate(page=page_global, per_page=3)
    return render_template('admin/products.html',apparel=apparel_data)

@admin.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        apparel_name = request.form.get('apparel_name')
        brand_name = request.form.get('brand_name')
        shop_name = request.form.get('shop_name')
        material_type = request.form.get('material_type')
        color = request.form.get('color')
        occasion_type = request.form.get('occasion_type')
        Price = request.form.get('Price')
        gender = request.form.get('shop_name')
        f = request.files['file']
        files=f.filename
        product = Apparels(apparel_name, brand_name, shop_name, files, material_type,color,occasion_type,gender,Price,"","")
        db.session.add(product)
        db.session.commit()
        flash("Successfully created!!")
        if f.filename != '':
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #f.save(secure_filename(f.filename))
            flash("Uploaded Successfully")
        else:
            flash(" Please select Images")
            return redirect(url_for('admin.dashboard'))

        return redirect(url_for('admin.dashboard'))