# Generated by Django 4.2.5 on 2023-10-05 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='category',
            field=models.CharField(choices=[('NEBULOSA', 'Nebulosa'), ('ESTRELA', 'Estrela'), ('GALÁXIA', 'Galáxia'), ('PLANETA', 'Planeta')], default='', max_length=100),
        ),
    ]
