# Generated by Django 4.2.2 on 2023-06-11 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reward', '0001_initial'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QrLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('timestamp', models.CharField(max_length=30)),
                ('quantity', models.PositiveIntegerField()),
                ('when_used', models.DateTimeField(auto_now_add=True)),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.store')),
            ],
        ),
        migrations.CreateModel(
            name='QrRewardLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reward.item')),
                ('qr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qr.qrlog')),
            ],
        ),
    ]