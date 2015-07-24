from translation_tool import app
from translation_tool.forms.signin_forms import SigninForm
from flask import render_template, session, redirect, url_for, request

@app.route('/signin', methods=['GET', 'POST'])
def signin():
	form = SigninForm()
	
	if request.method == 'POST':
		if form.validate() == False:
			if(len(form.email.errors) is 0):
				return render_template('signin.html', form = form, email = form.email.data)
			return render_template('signin.html', form = form, email = '')
		else:
			if form.validate_on_submit():
					session['remember_me'] = form.remember_me.data
			session['email'] = form.email.data
			return redirect(url_for('profile'))
															 
	elif request.method == 'GET':
		return render_template('signin.html', form = form, email = '')
