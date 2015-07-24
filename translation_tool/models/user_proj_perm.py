from translation_tool.models import db
from translation_tool.models.user import User
from translation_tool.models.project import Project

class UserProjPerm(db.Model):
	__tablename__ = 'user_project_permissions'
	user_id = db.Column(db.Integer, db.ForeignKey(User.user_id), primary_key=True)
	proj_id = db.Column(db.Integer, db.ForeignKey(Project.proj_id), primary_key=True)
	permission = db.Column(db.String(15))
	
	def __init__(self, permission):
		self.permission = permission.title()