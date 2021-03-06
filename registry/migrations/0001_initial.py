# Generated by Django 3.2.4 on 2021-06-18 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('address1', models.CharField(blank=True, max_length=100)),
                ('address2', models.CharField(blank=True, max_length=100)),
                ('address3', models.CharField(blank=True, max_length=100)),
                ('zippostal', models.CharField(blank=True, max_length=15)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('vat_number', models.CharField(blank=True, max_length=25)),
                ('cod_rea', models.CharField(blank=True, max_length=20)),
                ('email_bill', models.EmailField(blank=True, max_length=254)),
                ('email_sales', models.EmailField(blank=True, max_length=254)),
                ('email_tech', models.EmailField(max_length=254)),
                ('email_generic', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('mobile_phome', models.CharField(max_length=15)),
                ('contact_email', models.EmailField(max_length=254)),
                ('note', models.CharField(max_length=1000)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='registry.customer')),
            ],
        ),
    ]
