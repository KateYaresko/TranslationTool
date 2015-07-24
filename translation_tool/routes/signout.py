from translation_tool import app
from flask import session, redirect, url_for, request

@app.route('/signout')
def signout():    
	session.pop('email', None)
	return redirect(url_for('signin'))