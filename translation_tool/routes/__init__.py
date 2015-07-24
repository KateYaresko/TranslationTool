__all__ = ['retrieve_password', 'signup', 'signin', 'signout', 'navbar', 'profile', 'translate', 'project_properties']

from flask.ext.mail import Mail

mail = Mail()

from translation_tool.routes import *