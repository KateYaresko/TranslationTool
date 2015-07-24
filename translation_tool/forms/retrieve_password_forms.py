from flask.ext.wtf import Form
from wtforms import TextField, SubmitField, validators
from translation_tool.models.user import User


class RetrievePasswForm(Form):
	email = TextField("Email",    [validators.Required("Please enter your email address."), validators.Email("Incorrect email address.")])
	submit = SubmitField("save_new_passw")

	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)

	def validate(self):
		if not Form.validate(self):
			return False
		 
		user = User.query.filter_by(email = self.email.data.lower()).first()
		if user is not None:
			return True
		else:
			self.email.errors.append("Invalid email.")
			return False
