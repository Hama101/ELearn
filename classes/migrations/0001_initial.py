# Generated by Django 3.2.4 on 2021-12-05 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('mail', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('surname', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('mail', models.EmailField(blank=True, max_length=254, null=True)),
                ('situation', models.CharField(blank=True, max_length=50, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('nbr_heurs', models.IntegerField(blank=True, null=True)),
                ('_type', models.CharField(blank=True, max_length=50, null=True)),
                ('level', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_pro', models.EmailField(blank=True, max_length=254, null=True)),
                ('profile', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Seance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_hour', models.TimeField(blank=True, null=True)),
                ('end_hour', models.TimeField(blank=True, null=True)),
                ('salle_number', models.IntegerField(blank=True, null=True)),
                ('objective', models.CharField(blank=True, max_length=50, null=True)),
                ('tools', models.CharField(blank=True, max_length=50, null=True)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.group')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.subject')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='students',
            field=models.ManyToManyField(blank=True, null=True, to='classes.Student'),
        ),
    ]
