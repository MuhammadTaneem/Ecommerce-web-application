# Generated by Django 3.2.7 on 2022-06-28 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20220628_1640'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='author',
        ),
    ]
