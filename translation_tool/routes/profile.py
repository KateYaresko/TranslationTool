from translation_tool import app
from flask import render_template, redirect, session, url_for, request
from werkzeug import generate_password_hash
from validate_email import validate_email
from translation_tool.forms.profile_forms import EditPasswForm
from translation_tool.models.user import User
from translation_tool.models import db


@app.route('/profile', methods=['GET', 'POST'])
def profile():
	form = EditPasswForm()
	user = User.query.filter_by(email = session['email']).first()

	if request.method == 'POST':
		if 'change-passw-form' in request.form:
			if form.validate() == False:
				return render_template('profile.html', form=form, user=user, change_psw_error=True, change_psw=True)
			else:
				user.pwdhash = generate_password_hash(form.new_passw.data)

		elif request.form.get('form_name') == 'create-project':
			if request.form.get('name') == '':
				return 'Please enter name of project', 400
			return 'ok'

		elif 'delete-account-form' in request.form:
			db.session.delete(user)
			db.session.commit()
			return redirect(url_for('signout'))

		else:
			if request.form.get('name') == 'firstname-change':
				if request.form.get('value') == '':
					return 'Invalid first name', 400
				user.firstname = request.form.get('value')
			elif request.form.get('name') == 'lastname-change':
				if request.form.get('value') == '':
					return 'Invalid last name', 400
				user.lastname = request.form.get('value')
			elif request.form.get('name') == 'email-change':
				validated = validate_email(request.form.get('value'))
				if not validated:
					return 'Invalid email', 400
				session['email'] = request.form.get('value')
				user.email = request.form.get('value')
		
		db.session.commit()
		return render_template('profile.html', form=form, user = user, change_psw_error=False, change_psw=True)

	elif request.method == 'GET':
		if 'email' not in session or user is None:
			return redirect(url_for('signin'))
		else:
			return render_template('profile.html', user = user, form = form, change_psw_error=False, change_psw=False)