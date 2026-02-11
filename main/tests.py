from django.test import TestCase, Client
from django.urls import reverse

class MainViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_home_view(self):
        """Test home page view"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/home.html')
        self.assertContains(response, "Portfolio")
    
    def test_about_view(self):
        """Test about page view"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/about.html')
    
    def test_contact_view_get(self):
        """Test contact page GET request"""
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/contact.html')
        self.assertContains(response, "Kontaktiraj me")
    
    def test_contact_view_post_valid(self):
        """Test contact form with valid data"""
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'message': 'Test message for contact form'
        }
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(response.status_code, 302)
    
    def test_search_view(self):
        """Test search view"""
        response = self.client.get(reverse('search'), {'q': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/search.html')
    
    def test_api_docs_view(self):
        """Test API documentation view"""
        response = self.client.get(reverse('api_docs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'api_docs.html')