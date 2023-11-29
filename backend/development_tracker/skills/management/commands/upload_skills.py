"""Custom django-admin command to upload skills to database from csv."""

import csv

from django.core.management.base import BaseCommand

from skills.models import Skill


class Command(BaseCommand):
    """Command to upload skills to database from csv."""

    help = "Upload skills to database from csv"

    def add_arguments(self, parser):
        parser.add_argument("file", type=str, help="Path to the CSV file")

    def handle(self, *args, **options):
        file_path = options["file"]

        with open(file_path, "r") as csv_file:
            for row in csv.reader(csv_file):
                skill, created = Skill.objects.get_or_create(name=row[0])

                if created:
                    self.stdout.write(
                        self.style.SUCCESS(f'Skill "{row[0]}" has been created.')
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f'Skill "{row[0]}" already exists.')
                    )

        self.stdout.write(self.style.SUCCESS("Skills have been loaded successfully."))
