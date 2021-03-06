# Generated by Django 3.0.5 on 2020-04-24 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0012_auto_20200424_0102'),
    ]

    operations = [
        migrations.CreateModel(
            name='postQuote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_post', models.CharField(default='postQuote', max_length=20, verbose_name='Tipo de Post')),
                ('quote', models.CharField(max_length=100, verbose_name='Citação')),
                ('quote_author', models.CharField(max_length=25, verbose_name='Autor da Citação')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='summary_post',
            field=models.TextField(verbose_name='Resumo do Post, ou Citação'),
        ),
    ]
