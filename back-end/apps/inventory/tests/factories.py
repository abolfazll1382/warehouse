import factory
from factory.django import DjangoModelFactory

from apps.inventory.models import Category, InventoryItem


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f"Category {n}")


class InventoryItemFactory(DjangoModelFactory):
    class Meta:
        model = InventoryItem

    sku = factory.Sequence(lambda n: f"SKU-{n:04d}")
    name = factory.Faker("word")
    category = factory.SubFactory(CategoryFactory)
    quantity = 50
    unit = "pcs"
    reorder_threshold = 10
