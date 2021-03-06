# Generated by Django 2.2.10 on 2020-02-29 13:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0002_add_pg_trgm'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='building',
            options={'verbose_name': 'building', 'verbose_name_plural': 'buildings'},
        ),
        migrations.AlterModelOptions(
            name='csvfile',
            options={'verbose_name': 'CSV file', 'verbose_name_plural': 'CSV files'},
        ),
        migrations.AlterField(
            model_name='building',
            name='address',
            field=models.CharField(max_length=250, null=True, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='building',
            name='admin_update',
            field=models.DateField(blank=True, null=True, verbose_name='admin update'),
        ),
        migrations.AlterField(
            model_name='building',
            name='administration_update',
            field=models.DateField(blank=True, null=True, verbose_name='administration update'),
        ),
        migrations.AlterField(
            model_name='building',
            name='apartment_count',
            field=models.IntegerField(null=True, verbose_name='apartment count'),
        ),
        migrations.AlterField(
            model_name='building',
            name='cadastre_number',
            field=models.IntegerField(null=True, verbose_name='cadastre number'),
        ),
        migrations.AlterField(
            model_name='building',
            name='certified_expert',
            field=models.CharField(max_length=100, null=True, verbose_name='certified expert'),
        ),
        migrations.AlterField(
            model_name='building',
            name='county',
            field=models.CharField(max_length=60, verbose_name='county'),
        ),
        migrations.AlterField(
            model_name='building',
            name='created_on',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='created on'),
        ),
        migrations.AlterField(
            model_name='building',
            name='examination_year',
            field=models.IntegerField(null=True, verbose_name='examination year'),
        ),
        migrations.AlterField(
            model_name='building',
            name='general_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='general id'),
        ),
        migrations.AlterField(
            model_name='building',
            name='height_regime',
            field=models.CharField(max_length=50, null=True, verbose_name='height regime'),
        ),
        migrations.AlterField(
            model_name='building',
            name='land_registry_number',
            field=models.CharField(max_length=50, null=True, verbose_name='land registry number'),
        ),
        migrations.AlterField(
            model_name='building',
            name='lat',
            field=models.FloatField(null=True, verbose_name='latitude'),
        ),
        migrations.AlterField(
            model_name='building',
            name='lng',
            field=models.FloatField(null=True, verbose_name='longitude'),
        ),
        migrations.AlterField(
            model_name='building',
            name='locality',
            field=models.CharField(max_length=20, verbose_name='locality'),
        ),
        migrations.AlterField(
            model_name='building',
            name='observations',
            field=models.CharField(max_length=1000, null=True, verbose_name='observations'),
        ),
        migrations.AlterField(
            model_name='building',
            name='post_code',
            field=models.CharField(max_length=250, verbose_name='post code'),
        ),
        migrations.AlterField(
            model_name='building',
            name='registration_number',
            field=models.IntegerField(null=True, verbose_name='registration number'),
        ),
        migrations.AlterField(
            model_name='building',
            name='risk_category',
            field=models.CharField(db_index=True, max_length=50, verbose_name='risk category'),
        ),
        migrations.AlterField(
            model_name='building',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Choose'), (1, 'Accepted'), (-1, 'Rejected')], db_index=True, default=0, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='building',
            name='surface',
            field=models.FloatField(null=True, verbose_name='surface'),
        ),
        migrations.AlterField(
            model_name='building',
            name='year_built',
            field=models.IntegerField(null=True, verbose_name='year built'),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='file',
            field=models.FileField(upload_to='', verbose_name='file'),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='status',
            field=models.SmallIntegerField(choices=[(-1, 'Unsuccess'), (0, 'Not tried'), (1, 'Success')], default=0, editable=False, verbose_name='status'),
        ),
    ]
