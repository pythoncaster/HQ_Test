# Generated by Django 4.2.5 on 2023-10-04 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0007_remove_lessons_product_lessons_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lessons',
            name='product',
        ),
        migrations.AddField(
            model_name='lessons',
            name='product',
            field=models.ManyToManyField(to='system.product'),
        ),
    ]
