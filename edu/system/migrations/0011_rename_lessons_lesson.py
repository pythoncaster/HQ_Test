# Generated by Django 4.2.5 on 2023-10-04 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0010_remove_lessons_check_correct_remove_lessons_content_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lessons',
            new_name='Lesson',
        ),
    ]