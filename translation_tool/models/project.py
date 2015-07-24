from translation_tool.models import db

class Project(db.Model):
	__tablename__ = 'projects'
	proj_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(30))
	description = db.Column(db.String(255))
	
	def __init__(self, name, description):
		self.name = name
		self.description = description
