# Generated by Django 2.0.7 on 2018-07-25 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_web2', '0004_person_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
