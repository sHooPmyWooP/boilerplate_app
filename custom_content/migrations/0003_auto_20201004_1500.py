# Generated by Django 3.0.10 on 2020-10-04 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_content', '0002_auto_20201004_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plaintext',
            name='id',
            field=models.CharField(db_index=True, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
