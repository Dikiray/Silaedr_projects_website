# Generated by Django 3.0.4 on 2020-03-22 08:50

from django.db import migrations, models
import django_summernote.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
                ('project_text', django_summernote.fields.SummernoteTextField(verbose_name='project text')),
                ('project_picture', models.ImageField(blank=True, upload_to='projects_pics')),
            ],
        ),
    ]
