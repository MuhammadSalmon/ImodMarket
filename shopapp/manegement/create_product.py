from django.core.management.base import BaseCommand
from shopapp.models import Product

class Command(BaseCommand):
    help = 'Create products'

    def handle(self, *args, **options):
        self.stdout.write("Starting product creation")

        products_names = [
            "Laptop",
            "Desktop",
            "Smartphone",
        ]

        for product_name in products_names:
            product, created = Product.objects.get_or_create(name=product_name)
            if created:
                self.stdout.write(f"Product '{product_name}' created successfully")
            else:
                self.stdout.write(f"Product '{product_name}' already exists")

        self.stdout.write(self.style.SUCCESS("Product creation process completed"))