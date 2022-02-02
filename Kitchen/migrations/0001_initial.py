# Generated by Django 4.0.2 on 2022-02-02 14:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='KitchenModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_dishes', models.CharField(max_length=255)),
                ('photo', models.ImageField(blank=True, upload_to='photos/%y/%m/%d')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('ingredients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kitchen.ingredients')),
            ],
        ),
    ]