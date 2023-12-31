# Generated by Django 4.2.4 on 2023-09-22 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_quarter_studentgrade_hps_pt_total_score_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentgrade',
            name='gradelevel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='database.gradelevel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentgrade',
            name='section',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='database.section'),
            preserve_default=False,
        ),
    ]
