from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse


class Course(models.Model):
    name = models.CharField(max_length=1000)
    educator = models.CharField(max_length=100)
    num_lessons = models.PositiveSmallIntegerField(default=0)
    excerpt = models.TextField(max_length=300)
    description = RichTextField(blank=True, null=True)
    #description = models.TextField()
    picture = models.ImageField(upload_to='course_pictures')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])