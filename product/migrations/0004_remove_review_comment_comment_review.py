# Generated by Django 4.0.5 on 2022-07-07 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_review_comment_alter_review_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='review',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment_review', to='product.review', verbose_name='리뷰'),
        ),
    ]