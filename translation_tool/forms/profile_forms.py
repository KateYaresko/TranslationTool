from flask.ext.wtf import Form
from wtforms import SubmitField, validators, PasswordField
from werkzeug import check_password_hash
from translation_tool.models.user import User


class EditPasswForm(Form):
	old_passw = PasswordField("Old password",    [validators.Required("Please enter your current password. ")])
	new_passw = PasswordField("New password",    [validators.Required("Please enter your new password. ")])
	retype_new_passw = PasswordField("Retype new password",    [validators.Required("Please retype your new password. ")])
	submit = SubmitField("Save")
 
	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)
	
	def check_password(self, password):
		return check_password_hash(self.pwdhash, password)

	def validate(self):
		validated = True
		user = User.query.filter_by(email = session['email']).first()

		if not Form.validate(self):
			validated = False
		if user.check_password(self.old_passw.data) is False:
			self.old_passw.errors.append(" Invalid current password. ")
			validated = False
		if self.new_passw.data != self.retype_new_passw.data:
			self.retype_new_passw.errors.append(" Invalid retyping new password. ")
			validated = False
			
		return validated
