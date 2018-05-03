# Generated by Django 2.0.2 on 2018-04-18 06:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sn', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='factory',
            options={'verbose_name': 'Factory', 'verbose_name_plural': 'Factory'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': '产品型号', 'verbose_name_plural': '产品型号'},
        ),
        migrations.AlterModelOptions(
            name='record',
            options={'verbose_name': '申请记录', 'verbose_name_plural': '申请记录'},
        ),
        migrations.AddField(
            model_name='record',
            name='created_times',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Length has to be 12 and start with AC,like AC02345-1234', regex='^AC(\\d{5})-(\\d{4})$')]),
        ),
        migrations.AlterField(
            model_name='record',
            name='factory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='sn.Factory', verbose_name='Factory'),
        ),
        migrations.AlterField(
            model_name='record',
            name='total',
            field=models.PositiveIntegerField(verbose_name='Total'),
        ),
    ]