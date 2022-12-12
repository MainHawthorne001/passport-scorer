# Generated by Django 4.1.4 on 2022-12-09 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("scorer_weighted", "0001_initial"),
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Passport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("did", models.CharField(max_length=100, unique=True)),
                ("passport", models.JSONField(default=dict)),
                (
                    "version",
                    models.BigIntegerField(
                        blank=True,
                        db_index=True,
                        help_text="A counter for passport submissions. This records in which passport\n        submission the passport was updated. This will include also submissions when\n        stamps have been removed from this passport as part of de-duping",
                        null=True,
                    ),
                ),
                (
                    "community",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="passports",
                        to="account.community",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Score",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "score",
                    models.DecimalField(
                        blank=True, decimal_places=9, max_digits=18, null=True
                    ),
                ),
                (
                    "passport",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="score",
                        to="registry.passport",
                    ),
                ),
                (
                    "scorer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="scorer_weighted.scorer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Stamp",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("hash", models.CharField(db_index=True, max_length=100)),
                (
                    "provider",
                    models.CharField(db_index=True, default="", max_length=256),
                ),
                ("credential", models.JSONField(default=dict)),
                (
                    "community",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stamps",
                        to="account.community",
                    ),
                ),
                (
                    "passport",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stamps",
                        to="registry.passport",
                    ),
                ),
            ],
            options={
                "unique_together": {("hash", "community")},
            },
        ),
    ]
