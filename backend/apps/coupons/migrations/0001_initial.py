# Generated by Django 3.2.16 on 2023-10-09 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
        ('tiers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FixedPriceCoupon',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('discount_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('uses', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PercentageCoupon',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('discount_percentage', models.IntegerField()),
                ('uses', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('content_type', models.CharField(choices=[('courses', 'Courses'), ('products', 'Products'), ('tiers', 'Tiers'), ('games', 'Games'), ('music', 'Music'), ('videos', 'Videos'), ('movies', 'Movies'), ('assets', 'Assets'), ('art', 'Art'), ('software', 'Software'), ('licenseKeys', 'License Keys'), ('documents', 'Documents'), ('datasets', 'Datasets'), ('templates', 'Templates')], default='courses', max_length=20)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('fixed_price_coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coupons.fixedpricecoupon')),
                ('percentage_coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coupons.percentagecoupon')),
                ('tier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tiers.tier')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
