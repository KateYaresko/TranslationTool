from werkzeug import generate_password_hash, check_password_hash
from translation_tool.models import db

class User(db.Model):
	__tablename__ = 'users'
	user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	first_name = db.Column(db.String(100))
	last_name = db.Column(db.String(100))
	email = db.Column(db.String(120), unique=True)
	pwdhash = db.Column(db.String(100))
	
	def __init__(self, firstname, lastname, email, password):
		self.first_name = firstname.title()
		self.last_name = lastname.title()
		self.email = email.lower()
		self.set_password(password)
		
	def set_password(self, password):
		self.pwdhash = generate_password_hash(password)
	
	def check_password(self, password):
		return check_password_hash(self.pwdhash, password)