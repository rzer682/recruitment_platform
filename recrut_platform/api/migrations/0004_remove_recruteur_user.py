# Generated by Django 5.1.3 on 2024-11-26 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_candidat_user_alter_candidat_competences'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recruteur',
            name='user',
        ),
    ]
