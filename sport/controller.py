from typing import List
from sport.models import Sport


class SportController:
    def get_all(self) -> List[Sport]:
        return Sport.objects.all()

    def get_by_id(self, id: int) -> Sport:
        return Sport.objects.filter(id=id).get()

    def create(self, name: str, description: str) -> Sport:
        sport = Sport(name=name, description=description)
        sport.save()
        return sport

    def update(self, id: int, name: str, description: str) -> Sport:
        sport = self.get_by_id(id)
        sport.name = name
        sport.description = description
        sport.save()
        return sport

    def delete(self, id: int) -> None:
        sport = self.get_by_id(id)
        seller.delete()