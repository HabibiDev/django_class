from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from tags.models import TaggedItem
from django.urls import reverse

# Create your models here.

class Post(models.Model):

    STATUS_DRAFT = 10
    STATUS_PUBLISHED = 20
    STATUS_REJECTED = 30
    statuses = [
        (STATUS_DRAFT, 'Draft'),
        (STATUS_PUBLISHED, 'Published'),
        (STATUS_REJECTED, 'Rejected'),
        ]

    title = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey('Category', null = True, on_delete = models.CASCADE, related_name = 'posts')
    content = models.TextField(blank = True)
    keywords = models.TextField(max_length=500, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    status = models.IntegerField(choices = statuses, default = STATUS_DRAFT)
    tags = GenericRelation(TaggedItem)

    class Meta:
        ordering = ['-updated_on']

    def get_absolute_url(self):
        return reverse('posts:post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

class Category(models.Model):
    
    name = models.CharField(max_length = 120, unique = True)
    is_active = models.BooleanField()
    meta_keywords = models.TextField(blank = True)
    description = models.TextField(blank = True)

    def __str__(self):
        return self.name

