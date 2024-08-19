import json
import os
from django.core.management.base import BaseCommand, CommandError
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Load mock data from a JSON file into MongoDB'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the JSON file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        if not os.path.exists(file_path):
            raise CommandError(f'File "{file_path}" does not exist.')

        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError as e:
                raise CommandError(f'Invalid JSON file: {e}')

        client = MongoClient('mongodb://localhost:27017/')
        db = client['qmeter']
        collection = db['qmeter']

        if isinstance(data, list):
            collection.insert_many(data)
        else:
            collection.insert_one(data)
            
        client.close()

        self.stdout.write(self.style.SUCCESS('Mock data has been successfully loaded into MongoDB'))
