import json
from django.core.management.base import BaseCommand, CommandError, CommandParser
from dishes.models import Dish
from dishes.serializers import DishSerializer
from django.db import transaction


class Command(BaseCommand):
    help = "Loads data from a json file into the database."
    missing_args_message = "Provide either the relative path to manage.py of the file or the full path of the file."

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "path_to_json_file",
            type=str,
            help="Either the relative path to manage.py of the file or the full path of the file.",
        )

    def handle(self, *args, **options) -> str | None:
        try:
            json_file = open(options["path_to_json_file"], "r")
        except FileNotFoundError:
            raise CommandError(
                'File at "{}" does not exist.'.format(options["path_to_json_file"])
            )
        json_data = json.load(json_file)
        json_file.close()
        try:
            serializer = DishSerializer(data=json_data,many=True)
            assert serializer.is_valid()
            serializer.save()
        except AssertionError:
            return self.style.ERROR("Json data not compatible with database.")
        return self.style.SUCCESS("Successfully loaded json data into database.")
