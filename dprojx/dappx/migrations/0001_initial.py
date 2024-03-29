# Generated by Django 3.0.3 on 2021-07-17 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_summernote.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_direction', models.CharField(default='', max_length=200)),
                ('project_creators', models.CharField(default='', max_length=200)),
                ('project_state', models.CharField(default='0', max_length=1)),
                ('project_name', models.CharField(max_length=200)),
                ('project_root', models.CharField(max_length=200)),
                ('project_short', django_summernote.fields.SummernoteTextField(verbose_name='project short')),
                ('project_text', django_summernote.fields.SummernoteTextField(verbose_name='project text')),
                ('project_picture', models.ImageField(blank=True, upload_to='projects_pics')),
                ('project_acount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
