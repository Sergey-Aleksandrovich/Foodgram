# Generated by Django 3.1.2 on 2020-12-24 08:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_purchases'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchases',
            name='recipes',
        ),
        migrations.AddField(
            model_name='purchases',
            name='recipes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='recipes.recipes'),
            preserve_default=False,
        ),
    ]
