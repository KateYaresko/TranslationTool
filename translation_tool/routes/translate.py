from translation_tool import app
from flask import render_template

@app.route('/<project_id>/translate')
def translate(project_id):
	return render_template('translate.html')
