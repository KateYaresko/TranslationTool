from translation_tool import app
from flask import render_template, flash, redirect, url_for, request
from flask.ext.mail import Message
from translation_tool.forms.retrieve_password_forms import RetrievePasswForm
from translation_tool.models.user import User
from translation_tool.models import db
from translation_tool.routes import mail
import string, random


def id_generator(size = 15, chars = string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

@app.route('/retrieve_password', methods=['GET', 'POST'])
def retrieve_password():
	form = RetrievePasswForm()

	if request.method == 'POST':
		if form.validate() == False:
				return render_template('retrieve_password.html', form = form)
		user = User.query.filter_by(email = form.email.data).first()
		password = id_generator()
		msg = Message('Password Retrieve', sender = ("Translation Tool", "cw.translation.tool@gmail.com"), recipients = [form.email.data])
		msg.body = """
Hi %s,

A password reset request was made for your account. This is your new password: %s. You can change it on your profile page. 

Cheers,
Translation Tool Team""" % (user.firstname, password)
		mail.send(msg)
		user.pwdhash = generate_password_hash(password)
		db.session.commit()
		flash(u'Check your email, we have sent you a new password.', 'info')
		return redirect(url_for('signin'))

	elif request.method == 'GET':
		return render_template('retrieve_password.html', form = form)