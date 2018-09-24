import json

from django.core.management.base import BaseCommand

from sortdrinks.models import Category, Drink, Style


class Command(BaseCommand):
    help = "Update the database of drinks from a JSON file."

    def add_arguments(self, parser):
        parser.add_argument("file.json")

    def handle(self, *args, **kwargs):
        filename = kwargs["file.json"]
        with open(filename, 'r') as f:
            data = json.loads(f.read())

        items = data['items']

        for item in items:
            # Ignore unbuyable drinks
            if item['discontinued']:
                continue
            # Check if we already know about the item
            try:
                drink = Drink.objects.get(item_id=item['id'])
                # Update the price if different
                if drink.price != item['price']:
                    drink.price = item['price']
                    drink.save()
                continue
            except Drink.DoesNotExist:
                pass
            # Ignore alcohol free drinks
            alcohol = float(item['alcoholByVolume'][:-1])
            if not alcohol:
                continue
            category = Category.objects.get_or_create(name=item['group'])[0]
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
                price=item['price'],
                price_per_liter=item['pricePerLiter'],
                alcohol_percent=alcohol,
                volume=item['volume'],
                score=item['pricePerLiter'] / alcohol
            )
            drink.save()
