import os
import unittest
import tempfile
from flask import url_for
from app import app
from app import db
from app.authentication.models import User
import unittest

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class LogoutTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'test.db')
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_RECORD_QUERIES'] = True
        self.client = app.test_client()
        ctx = app.app_context()
        ctx.push()
        db.create_all()
        return app

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def initialize_test_user(self):
        usertest = User.query.filter(User.username == 'Testuser').first()
        if usertest==None:
            print 'Im inserting'
            user = User(username='testuser',
                   email='jordan.lazo@ucsp.edu.pe',
                   password='test',
                   role=1,
                   status=1
            )
            db.session.add(user)
            db.session.commit()
        else:
            print 'Nothing to do'

    def test_logout_remove_info(self):
        tester = app.test_client(self)
        response  = tester.get('/auth/logout', content_type='html/text')
        self.assertEqual(response.status_code, 301)

    def test_logout_redirect(self):
        self.initialize_test_user()
        tester = app.test_client(self)
        response = tester.post('/auth/logout/', content_type='html/text,', follow_redirects=True)

if __name__ == '__main__':
    unittest.main()
