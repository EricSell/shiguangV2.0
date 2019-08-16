# Generated by Django 2.2.4 on 2019-08-16 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Baike',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='百科名')),
                ('content', models.TextField(verbose_name='内容')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='index.User', verbose_name='用户')),
            ],
            options={
                'verbose_name': '百科',
                'verbose_name_plural': '百科',
                'db_table': 'baike',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('time', models.TimeField(auto_created=True, verbose_name='时间')),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='菜谱名')),
                ('content', models.TextField(verbose_name='内容')),
                ('descript', models.CharField(max_length=200, verbose_name='描述')),
                ('img', models.CharField(blank=True, max_length=255, null=True, verbose_name='图片')),
            ],
            options={
                'verbose_name': '菜谱',
                'verbose_name_plural': '菜谱',
                'db_table': 'menu',
            },
        ),
        migrations.CreateModel(
            name='Menutype',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('typename', models.CharField(max_length=20, verbose_name='菜谱分类')),
            ],
            options={
                'verbose_name': '菜谱类型',
                'verbose_name_plural': '菜谱类型',
                'db_table': 'menutype',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='主题分类名')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='find1.Menu', verbose_name='菜谱')),
            ],
            options={
                'verbose_name': '主题',
                'verbose_name_plural': '主题',
                'db_table': 'theme',
            },
        ),
        migrations.CreateModel(
            name='Shicai',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='食材分类名')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='find1.Menu', verbose_name='菜谱')),
            ],
            options={
                'verbose_name': '食材',
                'verbose_name_plural': '食材',
                'db_table': 'shicai',
            },
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='其他分类名')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='find1.Menu', verbose_name='菜谱')),
            ],
            options={
                'verbose_name': '其他分类',
                'verbose_name_plural': '其他分类',
                'db_table': 'other',
            },
        ),
        migrations.CreateModel(
            name='MenuShouLike',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('love', models.BooleanField(default=False, verbose_name='喜欢')),
                ('collect', models.BooleanField(default=False, verbose_name='收藏')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='find1.Menu', verbose_name='菜谱')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='index.User', verbose_name='用户')),
            ],
            options={
                'verbose_name': '菜谱喜欢收藏表',
                'verbose_name_plural': '菜谱喜欢收藏表',
                'db_table': 'menu_shou_like',
            },
        ),
        migrations.AddField(
            model_name='menu',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='find1.Menutype', verbose_name='菜谱类型'),
        ),
        migrations.AddField(
            model_name='menu',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='index.User', verbose_name='发表人'),
        ),
        migrations.CreateModel(
            name='Foodtype',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='饮食分类名')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='find1.Menu', verbose_name='菜谱')),
            ],
            options={
                'verbose_name': '饮食类型',
                'verbose_name_plural': '饮食类型',
                'db_table': 'foodtype',
            },
        ),
        migrations.CreateModel(
            name='BaikeShowLike',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('love', models.BooleanField(default=False, verbose_name='喜欢')),
                ('collect', models.BooleanField(default=False, verbose_name='收藏')),
                ('baike', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='find1.Baike', verbose_name='百科')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='index.User', verbose_name='用户')),
            ],
            options={
                'verbose_name': '百科喜欢收藏表',
                'verbose_name_plural': '百科喜欢收藏表',
                'db_table': 'baike_show_like',
            },
        ),
    ]
