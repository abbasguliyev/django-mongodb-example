import json
import os
from django.core.management.base import BaseCommand, CommandError
from pymongo import MongoClient
import pprint

class Command(BaseCommand):
    help = 'Load mock data from a JSON file into MongoDB'

    def handle(self, *args, **kwargs):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['qmeter']
        collection = db['qmeter']

        results = list(collection.find())
            
        client.close()

        self.stdout.write(self.style.SUCCESS(results))
