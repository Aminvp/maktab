# Generated by Django 3.2.9 on 2021-11-30 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='blog.Tag'),
        ),
    ]