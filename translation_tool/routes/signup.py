from translation_tool import app
from translation_tool.forms.signup_forms import SignupForm
from flask import render_template, flash, redirect, url_for, request
from flask.ext.mail import Message
from translation_tool.models.user import User
from translation_tool.models import db
from translation_tool.routes import mail


@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = SignupForm()
	
	if request.method == 'POST':
		if form.validate() == False:
			fname, lname, email = '', '', ''
			if len(form.firstname.errors) == 0:
				fname = form.firstname.data
			if len(form.lastname.errors) == 0:
				lname = form.lastname.data
			if len(form.email.errors) == 0:
				email = form.email.data
			return render_template('signup.html', form = form, fname = fname, lname = lname, email = email)
		else:
			newuser = User(form.firstname.data, form.lastname.data, form.email.data, password)
			db.session.add(newuser)
			db.session.commit()
			msg = Message('Welcome to Translation Tool!', sender=("Translation Tool", "cw.translation.tool@gmail.com"), recipients=[form.email.data])
			msg.body = """
Hi %s,

Your account has been successfully created! If it wasn't you, just ignore this message.
If it was you, use this temporary password to sign in: %s. You can change it on your profile page. 

Cheers,
Translation Tool Team""" % (form.firstname.data, password)
			mail.send(msg)
			flash(u'Check your email, we have sent you a password.', 'info')		
			return redirect(url_for('signin'))
	 
	elif request.method == 'GET':
		return render_template('signup.html', form=form)