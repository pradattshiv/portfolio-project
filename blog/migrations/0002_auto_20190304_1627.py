# Generated by Django 2.1.7 on 2019-03-04 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Body',
            field=models.TextField(),
        ),
    ]