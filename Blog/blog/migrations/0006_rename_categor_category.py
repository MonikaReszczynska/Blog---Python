# Generated by Django 4.0.3 on 2022-06-05 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_categor_post_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categor',
            new_name='Category',
        ),
    ]
