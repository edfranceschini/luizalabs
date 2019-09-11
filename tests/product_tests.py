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

    def test_product_list(self):
        response = self.app.get('/api/product/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_product_detail(self):
        response = self.app.get('/api/product/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_product_include(self):
        payload = {
            "title": 'Produto de teste automatizado',
            "price": 12.32,
            "image": '/media/image.png',
            "brand": 'teste de marca',
            "reviewScore": 10.0
        }
        response = self.app.post('/api/product/1', payload, follow_redirects=True)
        self.assertEqual(response.status_code, 201)

    def test_product_update(self):
        payload = {
            "title": 'Produto de teste automatizado',
            "price": 120.32,
            "image": '/media/image.png',
            "brand": 'teste de marca',
            "reviewScore": 15.0
        }
        response = self.app.put('/api/product/1', payload, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_product_delete(self):
        payload = {
            "title": 'Produto de teste automatizado',
            "price": 120.32,
            "image": '/media/image.png',
            "brand": 'teste de marca',
            "reviewScore": 15.0
        }
        response = self.app.put('/api/product/1', payload, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
