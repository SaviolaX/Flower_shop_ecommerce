# Generated by Django 4.0.3 on 2022-03-24 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
                ('category_image', models.ImageField(upload_to='category_images/')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_image', models.ImageField(upload_to='product_images/')),
                ('product_description', models.TextField()),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('product_created', models.DateTimeField(auto_now_add=True)),
                ('product_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.category')),
            ],
        ),
    ]