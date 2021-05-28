from flask import Flask, Blueprint, render_template
from flask_login import login_required, current_user

from ecommerce.model_admin import Apparels

app = Flask(__name__)

main = Blueprint('main', __name__)
@main.route('/home')
def home():
    return render_template('home.html')

@main.route('/shopping')
@login_required
def shopping():
    apparel_data = Apparels.query.all()
    apparel_data_by_men = Apparels.query.filter_by(material_type="men").all()
    apparel_data_by_women = Apparels.query.filter_by(material_type="women").all()
    apparel_data_by_sport = Apparels.query.filter_by(material_type="sport").all()
    apparel_data_by_electronic = Apparels.query.filter_by(material_type="electronic").all()
    return render_template('index.html',
                           data=apparel_data,
                           data_type=apparel_data_by_men,
                           data_type_women=apparel_data_by_women,
                           data_type_sport=apparel_data_by_sport,
                           data_type_electronic=apparel_data_by_electronic

                           )

@main.route('/food')
@login_required
def court():
    apparel_data = Apparels.query.all()
    apparel_data_by_men = Apparels.query.filter_by(material_type="men").all()
    apparel_data_by_women = Apparels.query.filter_by(material_type="women").all()
    apparel_data_by_sport = Apparels.query.filter_by(material_type="sport").all()
    apparel_data_by_electronic = Apparels.query.filter_by(material_type="electronic").all()
    return render_template('index.html',
                           data=apparel_data,
                           data_type=apparel_data_by_men,
                           data_type_women=apparel_data_by_women,
                           data_type_sport=apparel_data_by_sport,
                           data_type_electronic=apparel_data_by_electronic

                           )


@main.route('/movie')
@login_required
def movie():
    apparel_data = Apparels.query.all()
    apparel_data_by_men = Apparels.query.filter_by(material_type="men").all()
    apparel_data_by_women = Apparels.query.filter_by(material_type="women").all()
    apparel_data_by_sport = Apparels.query.filter_by(material_type="sport").all()
    apparel_data_by_electronic = Apparels.query.filter_by(material_type="electronic").all()
    return render_template('index.html',
                           data=apparel_data,
                           data_type=apparel_data_by_men,
                           data_type_women=apparel_data_by_women,
                           data_type_sport=apparel_data_by_sport,
                           data_type_electronic=apparel_data_by_electronic

                           )

