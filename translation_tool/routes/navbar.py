from translation_tool import app
from translation_tool.forms.navbar_forms import CreateProjectForm
from translation_tool.models.user import User
from flask import flash, render_template

@app.route('/navbar', methods=['POST'])
def navbar():
	form =  CreateProjectForm()
	user = User.query.filter_by(email = session['email']).first()

	if form.validate() == False:
		flash(u'Please enter the name of project', 'error')
		return render_template('layout_nav.html', form = form)
	else:
		return 'success'