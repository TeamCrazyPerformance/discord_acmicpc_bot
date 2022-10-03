# Generated by Django 4.1.1 on 2022-10-03 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acmicpc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submit',
            fields=[
                ('submit_id', models.IntegerField(primary_key=True, serialize=False)),
                ('result', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, related_name='submit', to='acmicpc.member')),
            ],
        ),
    ]
