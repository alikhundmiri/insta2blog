# Generated by Django 2.1.3 on 2018-11-09 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter_list',
            name='threshold',
            field=models.CharField(choices=[('landing-page', 'LANDING'), ('free-version', 'FREE'), ('paid-15', '15USD')], default='landing-page', max_length=20),
        ),
    ]
