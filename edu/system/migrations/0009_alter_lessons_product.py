# Generated by Django 4.2.5 on 2023-10-04 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0008_remove_lessons_product_lessons_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='product',
            field=models.ManyToManyField(blank=True, to='system.product'),
        ),
    ]
