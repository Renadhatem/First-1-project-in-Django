# Generated by Django 5.0.7 on 2024-07-10 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=255)),
                ('Content', models.TextField()),
                ('Category', models.CharField(max_length=255)),
                ('date_published', models.DateTimeField()),
            ],
        ),
    ]
