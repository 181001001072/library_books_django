# Generated by Django 4.1.1 on 2022-09-16 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_book_name_library_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='blog/app/media/Books'),
        ),
    ]