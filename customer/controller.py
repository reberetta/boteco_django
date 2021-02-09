from typing import List
from customer.models import Customer


class CustomerController:
    def get_all(self) -> List[Customer]:
        return Customer.objects.all()

    def get_by_id(self, id: int) -> Customer:
        return Customer.objects.filter(id=id).get()

    def create(self, name: str, description: str) -> Customer:
        customer = Customer(name=name, description=description)
        customer.save()
        return customer

    def update(self, id: int, name: str, description: str) -> Customer:
        customer = self.get_by_id(id)
        customer.name = name
        customer.description = description
        customer.save()
        return customer

    def delete(self, id: int) -> None:
        customer = self.get_by_id(id)
        seller.delete()