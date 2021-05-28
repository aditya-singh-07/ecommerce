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
    if current_user.is_authenticated:
        return render_template('admin/index.html')
    else:
        return render_template('admin/auth/login.html')

@admin.route('/admin/products')
def view_products():
    if current_user.is_authenticated:
        page_global = request.args.get('page', 1, type=int)
        apparel_data = Apparels.query.paginate(page=page_global, per_page=3)
        return render_template('admin/products.html',apparel=apparel_data)
    else:
        return render_template('admin/auth/login.html')

@admin.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if current_user.is_authenticated:
        if request.method == 'POST':
            apparel_name = request.form.get('apparel_name')
            brand_name = request.form.get('brand_name')
            shop_name = request.form.get('shop_name')
            material_type = request.form.get('material_type')
            color = request.form.get('color')
            occasion_type = request.form.get('occasion_type')
            Price = request.form.get('Price')
            gender = request.form.get('gender')
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
    else:
        return render_template('admin/auth/login.html')

@admin.route('/details/<int:product_id>/update', methods=['GET', 'POST'])
def product_updates(product_id):
    if current_user.is_authenticated:
        product_details = Apparels.query.get_or_404(product_id)
        if request.method == 'POST':
            product_details.apparel_name = request.form['apparel_name']
            product_details.brand_name = request.form['brand_name']
            product_details.shop_name = request.form['shop_name']
            product_details.material_type = request.form['material_type']
            product_details.color = request.form['color']
            product_details.occasion_type = request.form['occasion_type']
            product_details.Price = request.form['Price']
            product_details.gender = request.form['gender']
            db.session.add(product_details)
            db.session.commit()
            flash("Successfully updated!!")
            return redirect(url_for('admin.dashboard'))
        apparel_data = Apparels.query.get_or_404(product_id)
        return render_template('admin/edit.html',apparel=apparel_data,
                               name=current_user.username)
    else:
        return render_template('admin/auth/login.html')

@admin.route('/details/<int:product_id>/delete', methods=['GET', 'POST'])
def product_delete(product_id):
    if current_user.is_authenticated:
        vehicle_details = Apparels.query.get_or_404(product_id)
        db.session.delete(vehicle_details)
        db.session.commit()
        flash("Successfully Deleted!!")
        return redirect(url_for('admin.view_products'))
    else:
        return render_template('admin/auth/login.html')