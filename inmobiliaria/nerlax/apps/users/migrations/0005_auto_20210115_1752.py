# Generated by Django 3.1.4 on 2021-01-15 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_usermodel_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='user_type',
            field=models.CharField(blank=True, choices=[('1', 'CUSTOMER'), ('2', 'EMPLOYEE')], max_length=1, null=True),
        ),
    ]
