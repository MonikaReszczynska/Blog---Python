# Generated by Django 4.0.3 on 2022-06-07 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_categor_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click Lin kAbove To Read Blog Post', max_length=255),
        ),
    ]
