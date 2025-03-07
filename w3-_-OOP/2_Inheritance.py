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



if __name__ == "__main__":
    besiktas_as = BaseClub("BesiktasJK", "Turkey", 1903, "Black & White", "cArsi")
    besiktas_fc = FootballClub(besiktas_as, "Super League", "Besiktas Park", 41903)
    print(besiktas_fc.show_info())