# Generated by Django 5.0 on 2024-01-01 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0004_course_image_alter_course_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(null=True, upload_to='codeyad'),
        ),
    ]
