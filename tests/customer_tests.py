# project/test_basic.py


import os
import unittest

from luizalabs_flask import app, db

TEST_DB = 'test.db'


class BasicTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                                                os.path.join(
                                                    app.config['BASEDIR'],
                                                    TEST_DB)
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

        # Disable sending emails during unit testing
        self.assertEqual(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass

    ###############
    #### tests ####
    ###############

    def test_customer_list(self):
        response = self.app.get('/api/customer/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    def test_customer_include(self):
        payload = {
            "name": "Cliente de teste",
            "email": "teste@testes.com"
        }
        response = self.app.post('/api/customer/1',
                                 payload,
                                 follow_redirects=True)
        self.assertEqual(response.status_code, 201)


    def test_customer_detail(self):
        response = self.app.get('/api/customer/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    def test_customer_update(self):
        payload = {
            "name": "Cliente de teste alterado",
            "email": "teste@testes.com"
        }
        response = self.app.put('/api/customer/1',
                                payload,
                                follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_customer_delete(self):
        payload = {
            "name": "Cliente de teste alterado",
            "email": "teste@testes.com"
        }
        response = self.app.put('/api/product/1', payload, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
