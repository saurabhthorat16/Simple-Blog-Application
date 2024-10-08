# Generated by Django 4.2.13 on 2024-06-10 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hno', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('phoneNo', models.CharField(max_length=15)),
                ('addressDetails', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.address')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('photo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualificationName', models.CharField(max_length=255)),
                ('percentage', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=255)),
                ('fromDate', models.DateField()),
                ('toDate', models.DateField()),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='author_id',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.AddField(
            model_name='employee',
            name='projects',
            field=models.ManyToManyField(to='blog.project'),
        ),
        migrations.AddField(
            model_name='employee',
            name='qualifications',
            field=models.ManyToManyField(to='blog.qualification'),
        ),
        migrations.AddField(
            model_name='employee',
            name='workExperience',
            field=models.ManyToManyField(to='blog.workexperience'),
        ),
    ]
