# Generated by Django 5.0.1 on 2024-01-10 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spicy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('K', 'Kitap'), ('C', 'Çizgi Roman'), ('M', 'Manga'), ('EK', 'E-Kitap'), ('D', 'Dergi')], default='K', max_length=2),
            preserve_default=False,
        ),
    ]
