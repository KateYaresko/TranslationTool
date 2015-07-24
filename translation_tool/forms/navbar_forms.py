from flask.ext.wtf import Form
from wtforms import TextField, SubmitField, validators


class CreateProjectForm(Form):
	name = TextField("Name",    [validators.Required("Please enter the name of project.")])
	submit = SubmitField("submit")

	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)

	def validate(self):
		if not Form.validate(self):
			return False
		else:
			return True
