from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Project
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint koji omogućava pregled projekata.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['featured', 'technologies']
    search_fields = ['title', 'description', 'technologies']
    ordering_fields = ['completed_date', 'created_at', 'order']
    ordering = ['-featured', 'order', '-completed_date']
    
    @action(detail=True, methods=['post'])
    def increment_views(self, request, pk=None):
        """Povećava broj pregleda projekta"""
        project = self.get_object()
        project.views_count = project.views_count + 1
        project.save()
        return Response({'views': project.views_count})