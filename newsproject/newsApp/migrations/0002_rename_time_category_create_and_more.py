# Generated by Django 5.0.6 on 2024-05-23 19:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='time',
            new_name='create',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='created',
            new_name='createdby',
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(upload_to='static/images')),
                ('content', models.TextField()),
                ('published', models.BooleanField(default=False)),
                ('tags', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsApp.category')),
            ],
        ),
    ]
