# Generated by Django 4.2.7 on 2023-12-02 15:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("skills", "0002_alter_skillprogress_skill"),
    ]

    operations = [
        migrations.AddField(
            model_name="skill",
            name="description",
            field=models.CharField(
                default="description",
                help_text="Skill's description",
                max_length=300,
                verbose_name="description",
            ),
            preserve_default=False,
        ),
    ]
