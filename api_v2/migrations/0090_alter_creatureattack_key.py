# Generated by Django 3.2.20 on 2024-05-31 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0089_rename_creature_action_creatureattack_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creatureattack',
            name='key',
            field=models.CharField(help_text='Unique key for the Document.', max_length=100, primary_key=True, serialize=False),
        ),
    ]
