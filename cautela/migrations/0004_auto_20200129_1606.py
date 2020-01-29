# Generated by Django 2.2.7 on 2020-01-29 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cautela', '0003_auto_20200128_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='cautela',
            name='quantidade_emprestada',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='cautela',
            name='data_de_devolucao',
            field=models.DateField(blank=True, null=True),
        ),
    ]