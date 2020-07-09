from django.db import models

# Create your models here.
from django.db import models
from django_summernote.fields import SummernoteTextField
# Create your models here.
from django.contrib.auth.models import User
class ProjectInfo(models.Model):
    project_direction = models.CharField(max_length = 200, default = '')
    project_creators = models.CharField(max_length = 200, default = '')
    project_state = models.CharField(max_length = 1, default = '0')
    project_name = models.CharField(max_length = 200)
    project_text = SummernoteTextField(verbose_name="project text")
    project_picture = models.ImageField(upload_to='projects_pics',blank=True)
    def __str__(self):
        return self.project_name
