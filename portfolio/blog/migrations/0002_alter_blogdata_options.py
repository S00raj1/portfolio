# Generated by Django 4.2.3 on 2023-07-27 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogdata',
            options={'ordering': ('publication_date',)},
        ),
    ]
