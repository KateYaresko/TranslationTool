from translation_tool import app
from flask import render_template

@app.route('/<project_id>/project_properties')
def project_properties(project_id):
	return render_template('project_properties.html')