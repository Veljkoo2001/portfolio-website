from django.db import models
from django.urls import reverse
from .managers import ProjectManager

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Naslov")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL slug")
    description = models.TextField(verbose_name="Opis")
    short_description = models.CharField(max_length=300, verbose_name="Kratak opis")
    
    # Tehnologije (čuvamo kao string, kasnije možemo kao ManyToMany)
    technologies = models.CharField(max_length=200, verbose_name="Tehnologije")
    
    # Slike
    image = models.ImageField(upload_to='projects/images/', verbose_name="Glavna slika")
    screenshot_1 = models.ImageField(upload_to='projects/screenshots/', blank=True, null=True, verbose_name="Screenshot 1")
    screenshot_2 = models.ImageField(upload_to='projects/screenshots/', blank=True, null=True, verbose_name="Screenshot 2")
    
    # Linkovi
    github_url = models.URLField(blank=True, verbose_name="GitHub link")
    live_url = models.URLField(blank=True, verbose_name="Live demo link")
    
    # Status
    featured = models.BooleanField(default=False, verbose_name="Istaknuti projekt")
    completed_date = models.DateField(verbose_name="Datum završetka")
    
    # Ordering
    order = models.IntegerField(default=0, verbose_name="Redosled")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    views_count = models.PositiveIntegerField(default=0, verbose_name="Broj pregleda")

    class Meta:
        ordering = ['order', '-completed_date']
        verbose_name = "Projekat"
        verbose_name_plural = "Projekti"
        indexes = [
            models.Index(fields=['featured', 'completed_date']),
            models.Index(fields=['slug']),
            models.Index(fields=['technologies']),
        ]
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("projects:project_detail", kwargs={"slug": self.slug})
    
    def technologies_list(self):
        """Vraća listu tehnologija"""
        return [tech.strip() for tech in self.technologies.split(',')]
    
    objects = ProjectManager()