# Generated by Django 3.2 on 2021-04-08 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('symbol', models.CharField(max_length=10)),
                ('market_cap', models.BigIntegerField(default=0)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['price'],
            },
        ),
    ]
