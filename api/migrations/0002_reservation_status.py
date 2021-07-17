# Generated by Django 3.2.5 on 2021-07-17 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('PD', 'Pendiente'), ('PG', 'Pagado'), ('EL', 'Eliminado')], default='PD', max_length=2),
        ),
    ]
