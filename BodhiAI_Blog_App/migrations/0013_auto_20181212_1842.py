# Generated by Django 2.1.3 on 2018-12-12 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BodhiAI_Blog_App', '0012_blog_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]