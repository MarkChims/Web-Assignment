# Generated by Django 5.1.1 on 2024-10-07 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
