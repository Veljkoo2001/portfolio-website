from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    technologies_list = serializers.SerializerMethodField()
    
    class Meta:
        model = Project
        fields = [
            'id', 'title', 'slug', 'short_description', 
            'description', 'technologies', 'technologies_list',
            'image', 'github_url', 'live_url', 'featured',
            'completed_date', 'created_at', 'views_count'
        ]
        read_only_fields = ['slug', 'created_at', 'views_count']
    
    def get_technologies_list(self, obj):
        return obj.technologies_list()