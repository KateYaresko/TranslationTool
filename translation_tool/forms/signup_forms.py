from flask.ext.wtf import Form
from wtforms import TextField, SubmitField, validators
from translation_tool.models.user import User


class SignupForm(Form):
	firstname = TextField("First name",    [validators.Required("Please enter your first name. ")])
	lastname = TextField("Last name",    [validators.Required("Please enter your last name. ")])
	email = TextField("Email",    [validators.Required("Please enter your email address. "), validators.Email("Incorrect email address. ")])
	submit = SubmitField("Sign up")
 
	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)
 
	def validate(self):
		if not Form.validate(self):
			return False
		 
		user = User.query.filter_by(email = self.email.data.lower()).first()
		if user == None:
			self.email.errors.append("This email is already taken")
			return False
		else:
			return True
