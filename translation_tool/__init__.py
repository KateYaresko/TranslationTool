from flask import Flask
 
app = Flask(__name__)

app.secret_key = "sjdfsorcfhm85m398q29JKOIHi840KDJ28401-VOKRG=1239NL123jdo"
 
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'cw.translation.tool@gmail.com'
app.config["MAIL_PASSWORD"] = 'seanshosh'

from routes import mail
mail.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ttuser:ttpassw@localhost/translation'
 
from models import db
db.init_app(app)
 
import translation_tool.routes