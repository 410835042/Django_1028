# Generated by Django 3.2.9 on 2022-10-28 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(blank=True, null=True, to='products.Size'),
        ),
    ]
