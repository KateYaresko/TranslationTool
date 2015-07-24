from flask.ext.wtf import Form
from wtforms import TextField, SubmitField, validators, PasswordField, BooleanField
from translation_tool.models.user import User

class SigninForm(Form):
	email = TextField("Email",    [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
	password = PasswordField('Password', [validators.Required("Please enter a password.")])
	remember_me = BooleanField('remember_me', default=False)
	submit = SubmitField("Sign In")
	 
	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)
 
	def validate(self):
		if not Form.validate(self):
			return False
		 
		user = User.query.filter_by(email = self.email.data.lower()).first()
		if user and user.check_password(self.password.data):
			return True
		else:
			self.email.errors.append("Invalid email or password")
			return False
