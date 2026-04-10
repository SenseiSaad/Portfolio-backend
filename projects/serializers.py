from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=['id', 'category', 'title','short_description','description','tech_stack','github_link','live_link','created_at']
