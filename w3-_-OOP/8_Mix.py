from abc import ABC, abstractmethod

class BaseClub:
    def __init__(self, club_name, country, founded_year, colors, fans_group):
        self.club_name = club_name
        self.country = country
        self.founded_year = founded_year
        self.colors = colors
        self.fans_group = fans_group
    
    def show_info(self):
        return f"Club Name: {self.club_name}\nCountry: {self.country}\nFounded Year: {self.founded_year}\nColors: {self.colors}\nFan Group: {self.fans_group}"





class FootballClub(BaseClub):
    def __init__(self, base_club, league, stadium_name, stadium_capacity):
        super().__init__(
            club_name=base_club.club_name,
            country=base_club.country,
            founded_year=base_club.founded_year,
            colors=base_club.colors,
            fans_group=base_club.fans_group
        )
        self.league = league
        self.stadium_name = stadium_name
        self.stadium_capacity = stadium_capacity

    def show_info(self):
        return f"{super().show_info()}\nLeague: {self.league}\nStadium: {self.stadium_name}\nStadium Capacity: {self.stadium_capacity}"





class ClubStaff(FootballClub):
    def __init__(self, football_club, president_name, department_name_1, department_name_2):
        super().__init__(
            base_club=football_club,
            league=football_club.league,
            stadium_name=football_club.stadium_name,
            stadium_capacity=football_club.stadium_capacity
        )
        self.president_name = president_name
        self.__department_name_1 = department_name_1
        self.__department_name_2 = department_name_2
    
    def get_department_name_1(self):
        return self.__department_name_1
    
    def set_department_name_1(self, department_name_1):
        self.__department_name_1 = department_name_1

    def get_department_name_2(self):
        return self.__department_name_2
    
    def set_department_name_2(self, department_name_2):
        self.__department_name_2 = department_name_2

    def show_info(self):
        return f"{super().show_info()}\n"

    def show_department_info(self):
        return f"President: {self.president_name}\nDepartment 1: {self.get_department_name_1()}\nDepartment 2: {self.get_department_name_2()}"





class TechnicalTeam(ClubStaff):
    def __init__(self, club_staff, technic_director, assistant_coach_1, assistant_coach_2, goalkeeper_coach, analysis_coach):
        super().__init__(
            football_club=club_staff,
            president_name=club_staff.president_name,
            department_name_1=club_staff.get_department_name_1(),
            department_name_2=club_staff.get_department_name_2()
        )
        self.technic_director = technic_director
        self.assistant_coach_1 = assistant_coach_1
        self.assistant_coach_2 = assistant_coach_2
        self.goalkeeper_coach = goalkeeper_coach
        self.analysis_coach = analysis_coach

    def show_info(self):
        return f"{super().show_info()}"
    
    def show_department_info(self):
        return f"Technical Director: {self.technic_director}\nAssistant Coach 1: {self.assistant_coach_1}\nAssistant Coach 2: {self.assistant_coach_2}\nGoalkeeper Coach: {self.goalkeeper_coach}\nAnalysis Coach: {self.analysis_coach}"






class ScoutTeam(ClubStaff):
    def __init__(self, club_staff, chef_scout, scout):
        super().__init__(
            football_club=club_staff,
            president_name=club_staff.president_name,
            department_name_1=club_staff.get_department_name_1(),
            department_name_2=club_staff.get_department_name_2()
        )
        self.chef_scout = chef_scout
        self.scout = scout

    def show_info(self):
        return f"{super().show_info()}"
    
    def show_department_info(self):
        return f"Chief Scout: {self.chef_scout}\nScout: {self.scout}"



# ---------------------------------------------------------------- #




print("################################")
print("Company\n")
besiktas_as = BaseClub("BesiktasJK", "Turkey", 1903, "Black & White", "cArsi")
print(besiktas_as.show_info())


print("\n################################")
print("Football Club\n")
besiktas_fc = FootballClub(
    base_club=besiktas_as,
    league="Super League",
    stadium_name="Besiktas Park",
    stadium_capacity=41903
)
print(besiktas_fc.show_info())


print("\n################################")
print("Club Staff\n")
besiktas_staff = ClubStaff(
    football_club=besiktas_fc,
    president_name="Serdar Adali",
    department_name_1="Technical Department",
    department_name_2="Scouting Department"
)
print(besiktas_staff.show_department_info())


print("\n################################")
print("Technical Team\n")
besiktas_tech = TechnicalTeam(
    club_staff=besiktas_staff,
    technic_director="Ole Gunnar Solskjaer",
    assistant_coach_1="Erling Moe",
    assistant_coach_2="Mike Marsh",
    goalkeeper_coach="Richard John Hartis",
    analysis_coach="Thomas Antony Green"
)
print(besiktas_tech.show_department_info())


print("\n################################")
print("Scout Team\n")
besiktas_scout = ScoutTeam(
    club_staff=besiktas_staff,
    chef_scout="Eduard Graf",
    scout="John Vik"
)
print(besiktas_scout.show_department_info())
print()