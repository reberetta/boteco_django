from typing import List
from team.models import Team


class TeamController:
    def get_all(self) -> List[Team]:
        return Team.objects.all()

    def get_by_id(self, id: int) -> Team:
        return Team.objects.filter(id=id).get()

    def create(self, name: str, description: str) -> Team:
        team = Team(name=name, description=description)
        team.save()
        return team

    def update(self, id: int, name: str, description: str) -> Team:
        team = self.get_by_id(id)
        team.name = name
        team.description = description
        team.save()
        return team

    def delete(self, id: int) -> None:
        team = self.get_by_id(id)
        seller.delete()