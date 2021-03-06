# Generated by Django 2.1.3 on 2018-12-18 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BodhiAI_Blog_App', '0018_auto_20181218_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('Comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='BodhiAI_Blog_App.Blog')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='BodhiAI_Blog_App.Comment')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.RemoveField(
            model_name='news',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='news',
            name='user',
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]
