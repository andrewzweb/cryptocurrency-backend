# Generated by Django 3.2 on 2021-04-12 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_dashboard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboard',
            name='currency',
        ),
        migrations.AddField(
            model_name='dashboard',
            name='currency',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='currency.currency'),
            preserve_default=False,
        ),
    ]
