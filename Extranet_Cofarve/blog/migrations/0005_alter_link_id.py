# Generated by Django 4.0.4 on 2022-05-18 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_linksecond_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
