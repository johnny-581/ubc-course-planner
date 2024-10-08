# Generated by Django 5.0.8 on 2024-09-13 03:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courselist', '0005_course_credits'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usercourse',
            unique_together={('user', 'course'), ('user', 'order')},
        ),
    ]
