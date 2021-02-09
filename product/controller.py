from typing import List
from product.models import Product


class ProductController:
    def get_all(self) -> List[Product]:
        return Product.objects.all()

    def get_by_id(self, id: int) -> Product:
        return Product.objects.filter(id=id).get()

    def create(self, name: str, description: str) -> Product:
        product = Product(name=name, description=description)
        product.save()
        return product

    def update(self, id: int, name: str, description: str) -> Product:
        product = self.get_by_id(id)
        product.name = name
        product.description = description
        product.save()
        return product

    def delete(self, id: int) -> None:
        product = self.get_by_id(id)
        seller.delete()