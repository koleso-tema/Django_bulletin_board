# Generated by Django 4.2.1 on 2023-06-06 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0003_alter_response_announcement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='announcement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='anno_to_ammo', to='announcement.announcement'),
        ),
        migrations.AlterField(
            model_name='response',
            name='dateCreation',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]