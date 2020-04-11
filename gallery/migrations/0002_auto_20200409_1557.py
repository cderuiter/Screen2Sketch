# Generated by Django 3.0.5 on 2020-04-09 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='sigma',
            field=models.DecimalField(decimal_places=0, default=6, max_digits=10),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
