# Generated by Django 2.1.3 on 2018-12-19 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BodhiAI_Blog_App', '0030_auto_20181219_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='BodhiAI_Blog_App.Blog'),
        ),
    ]
