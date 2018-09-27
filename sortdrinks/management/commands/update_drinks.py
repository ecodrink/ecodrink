import json

from django.core.management.base import BaseCommand

from sortdrinks.models import Category, Drink, Style, Country


class Command(BaseCommand):
    help = "Update the database of drinks from a JSON file."

    def add_arguments(self, parser):
        parser.add_argument("file.json")

    def handle(self, *args, **kwargs):
        filename = kwargs["file.json"]
        with open(filename, 'r') as f:
            data = json.loads(f.read())

        items = data['items']
        drinks = []

        for item in items:
            # Ignore unbuyable drinks
            if item['discontinued']:
                continue
            # Ignore alcohol free drinks
            alcohol = float(item['alcoholByVolume'][:-1])
            if not alcohol:
                continue
            # Check if we already know about the item
            try:
                drink = Drink.objects.get(item_id=item['id'])
                if item['discontinued']:
                    # Remove old drinks
                    drink.delete()
                elif drink.price != item['price']:
                    # Update the price if different
                    drink.price = item['price']
                    drink.score = item['pricePerLiter'] / alcohol
                    drink.save()
                continue
            except Drink.DoesNotExist:
                pass
            category = Category.objects.get_or_create(name=item['group'])[0]
            country = Country.objects.get_or_create(name=item['countryOfOrigin'])[0]
            if item['style']:
                style = Style.objects.get_or_create(name=item['style'])[0]
            else:
                style = None
            name = item['name']
            if item['name2']:
                name += f" - {item['name2']}"
            drink = Drink(
                item_id=item['id'],
                name=name,
                category=category,
                style=style,
                organic=item['organic'],
                country=country,
                price=item['price'],
                alcohol_percent=alcohol,
                volume=item['volume'],
                score=item['pricePerLiter'] / alcohol
            )
            drinks.append(drink)
        Drink.objects.bulk_create(drinks)
