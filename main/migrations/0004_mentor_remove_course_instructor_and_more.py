# Generated by Django 5.1.3 on 2024-12-12 05:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_course_category_course_is_free_userprofileinfo_exp_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('experience', models.TextField()),
                ('skills', models.JSONField()),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='instructor',
        ),
        migrations.AlterField(
            model_name='material',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='mentor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='main.mentor'),
            preserve_default=False,
        ),
    ]
