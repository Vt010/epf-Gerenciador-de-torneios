from bottle import request, template, redirect
from models.user import User
import json

class DashboardController:
    def __init__(self, app):
        self.app = app
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/dashboard', method='GET', callback=self.dashboard)

    def dashboard(self):
        user_cookie = request.get_cookie('user')
        if not user_cookie:
            return redirect('/login')

        try:
            user_dict = json.loads(user_cookie)
            user = User.from_dict(user_dict)
        except:  
            return redirect('/login')

        return template('dashboard', user=user)
