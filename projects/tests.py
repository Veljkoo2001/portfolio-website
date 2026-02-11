from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Project
import tempfile
from PIL import Image
import os

class ProjectModelTest(TestCase):
    def setUp(self):
        # Kreiraj testnu sliku
        self.test_image = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False)
        self.test_image.close()
        image = Image.new('RGB', (100, 100), color='red')
        image.save(self.test_image.name)
        
        self.project = Project.objects.create(
            title="Test Project",
            slug="test-project",
            short_description="Test short description",
            description="Test full description",
            technologies="Django, Python, Bootstrap",
            github_url="https://github.com/test/test",
            live_url="https://test.com",
            featured=True,
            completed_date="2023-01-01",
            order=1
        )
        self.project.image.name = self.test_image.name
    
    def tearDown(self):
        # Obriši testnu sliku
        os.unlink(self.test_image.name)
    
    def test_project_creation(self):
        """Test da li se projekt pravilno kreira"""
        self.assertEqual(self.project.title, "Test Project")
        self.assertEqual(self.project.slug, "test-project")
        self.assertTrue(self.project.featured)
    
    def test_project_str_method(self):
        """Test __str__ method"""
        self.assertEqual(str(self.project), "Test Project")
    
    def test_technologies_list_method(self):
        """Test technologies_list method"""
        tech_list = self.project.technologies_list()
        self.assertEqual(len(tech_list), 3)
        self.assertIn("Django", tech_list)
    
    def test_get_absolute_url(self):
        """Test get_absolute_url method"""
        url = self.project.get_absolute_url()
        self.assertEqual(url, reverse('projects:project_detail', kwargs={'slug': self.project.slug}))

class ProjectViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.project = Project.objects.create(
            title="Test View Project",
            slug="test-view-project",
            short_description="Test",
            description="Test",
            technologies="Django",
            completed_date="2023-01-01"
        )
    
    def test_project_list_view(self):
        """Test project list view"""
        response = self.client.get(reverse('projects:project_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/list.html')
        self.assertContains(response, "Test View Project")
    
    def test_project_detail_view(self):
        """Test project detail view"""
        response = self.client.get(reverse('projects:project_detail', kwargs={'slug': self.project.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/detail.html')
        self.assertContains(response, self.project.title)
    
    def test_project_detail_view_404(self):
        """Test 404 za nepostojeći projekt"""
        response = self.client.get(reverse('projects:project_detail', kwargs={'slug': 'non-existent'}))
        self.assertEqual(response.status_code, 404)

class ProjectAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        self.project = Project.objects.create(
            title="API Test Project",
            slug="api-test-project",
            short_description="API Test",
            description="API Test Description",
            technologies="Django, REST",
            completed_date="2023-01-01"
        )
    
    def test_api_project_list(self):
        """Test API project list endpoint"""
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
    
    def test_api_project_detail(self):
        """Test API project detail endpoint"""
        response = self.client.get(f'/api/projects/{self.project.id}/')
        self.assertEqual(response.status_code, 200)
    
    def test_api_search(self):
        """Test API search functionality"""
        response = self.client.get('/api/projects/?search=Django')
        self.assertEqual(response.status_code, 200)