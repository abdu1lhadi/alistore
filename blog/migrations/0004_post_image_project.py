# Generated by Django 2.2.3 on 2019-07-06 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190530_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_project',
            field=models.ImageField(default='default.jpg', upload_to='post_co'),
        ),
    ]
