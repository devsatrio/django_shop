# Generated by Django 2.2 on 2020-01-11 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kategori',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='barang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=70)),
                ('deskripsi', models.TextField()),
                ('stok', models.IntegerField()),
                ('diskon', models.IntegerField()),
                ('harga', models.IntegerField()),
                ('kategori', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='produk.kategori')),
            ],
        ),
    ]