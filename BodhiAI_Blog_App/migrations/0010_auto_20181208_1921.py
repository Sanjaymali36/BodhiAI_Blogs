# Generated by Django 2.1.3 on 2018-12-08 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BodhiAI_Blog_App', '0009_auto_20181208_1913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='link_url',
            new_name='link1',
        ),
        migrations.AddField(
            model_name='blog',
            name='link2',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='link3',
            field=models.URLField(null=True),
        ),
    ]
