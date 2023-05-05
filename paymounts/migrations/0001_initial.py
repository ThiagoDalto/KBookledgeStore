from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("billets", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Paymount",
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=64, null=True)),
                ('status', models.CharField(max_length=64)),
                ('value', models.PositiveSmallIntegerField()),
                ('payment_method', models.CharField(choices=[(1, 'BOLETO'), (2, 'CREDIT_CARD'), (3, 'DEBIT_CARD')], default=1, max_length=64)),
                ('created_at', models.DateTimeField()),
                ('paid_at', models.DateTimeField(null=True)),
                ('card', models.CharField(max_length=7, null=True)),
                ('link_billet_pdf', models.TextField()),
                ('link_billet_png', models.TextField()),
                ('billet', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paymount', to='billets.billet')),
            ],
        ),
    ]
