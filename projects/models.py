from django.db import models

class Project(models.Model):

    CATEGORY_CHOICES = [
        ('personal', 'Personal Project'),
        ('experience', 'Work Experience'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='personal')
    title=models.CharField(max_length=200)
    short_description=models.CharField(max_length=300, default='', blank=True)
    description=models.TextField()
    tech_stack=models.CharField(max_length=500)
    github_link=models.URLField()
    live_link=models.URLField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
