from abc import ABC, abstractmethod

class TeamMember(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def role_description(self):
        pass

class Coach(TeamMember):
    def role_description(self):
        return f"{self.name} is responsible for training the team."

class Scout(TeamMember):
    def role_description(self):
        return f"{self.name} is responsible for finding new talents."


if __name__ == "__main__":
    coach = Coach("Ole Gunnar Solskjaer")
    scout = Scout("Eduard Graf")
    print(coach.role_description())
    print(scout.role_description())