# Generated by Django 2.2.6 on 2020-01-07 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200107_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='date_created',
            field=models.DateTimeField(),
        ),
    ]