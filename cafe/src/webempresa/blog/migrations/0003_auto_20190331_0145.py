# Generated by Django 2.1.7 on 2019-03-31 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190327_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='get_posts', to='blog.Category', verbose_name='Fecha de creación'),
        ),
    ]
