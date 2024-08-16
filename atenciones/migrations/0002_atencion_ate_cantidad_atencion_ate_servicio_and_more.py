# Generated by Django 4.2.15 on 2024-08-15 04:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('servicios', '0002_alter_servicio_ser_nombre'),
        ('atenciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='atencion',
            name='ate_cantidad',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='atencion',
            name='ate_servicio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='servicios.servicio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='atencion',
            name='ate_usuario',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='DetalleAtencion',
        ),
    ]
