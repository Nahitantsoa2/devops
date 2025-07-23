import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    
    def setUp(self):
        """Set up test client before each test"""
        self.app = app.test_client()
        self.app.testing = True
    
    def test_home_route_status_code(self):
        """Test that the home route returns status code 200"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_home_route_content_type(self):
        """Test that the home route returns HTML content"""
        response = self.app.get('/')
        self.assertEqual(response.content_type, 'text/html; charset=utf-8')
    
    def test_home_route_contains_bonjour(self):
        """Test that the home route contains 'Bonjour tout le monde'"""
        response = self.app.get('/')
        self.assertIn(b'Bonjour tout le monde', response.data)
    
    def test_home_route_contains_html_structure(self):
        """Test that the response contains proper HTML structure"""
        response = self.app.get('/')
        self.assertIn(b'<!DOCTYPE html>', response.data)
        self.assertIn(b'<html lang="fr">', response.data)
        self.assertIn(b'<title>Bonjour Flask</title>', response.data)
    
    def test_home_route_contains_styling(self):
        """Test that the response contains CSS styling"""
        response = self.app.get('/')
        self.assertIn(b'<style>', response.data)
        self.assertIn(b'font-family: Arial', response.data)
    
    def test_template_encoding(self):
        """Test that the template has proper UTF-8 encoding"""
        response = self.app.get('/')
        self.assertIn(b'charset="UTF-8"', response.data)

if __name__ == '__main__':
    unittest.main()
