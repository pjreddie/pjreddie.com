# Generated by Django 2.1.1 on 2018-09-10 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_page_subslug'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='base',
            field=models.BooleanField(default=True),
        ),
    ]
