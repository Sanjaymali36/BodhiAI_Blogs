# Generated by Django 2.1.3 on 2018-12-08 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BodhiAI_Blog_App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='category',
            new_name='board',
        ),
    ]
