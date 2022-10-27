# Generated by Django 4.1.2 on 2022-10-26 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freeshelf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50)),
                ('author', models.TextField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('url', models.URLField(null=True, unique=True)),
                ('created_at', models.DateTimeField(null=True)),
            ],
        ),
    ]