class BaseClub:
    def __init__(self, club_name):
        self.club_name = club_name
    
    def show_info(self):
        return f"Club Name: {self.club_name}"

class FootballClub(BaseClub):
    def __init__(self, base_club, league):
        super().__init__(base_club.club_name)
        self.league = league

    def show_info(self):
        return f"{super().show_info()}\nLeague: {self.league}"


if __name__ == "__main__":
    besiktas_as = BaseClub("BesiktasJK")
    besiktas_fc = FootballClub(besiktas_as, "Super League")
    print("(BaseClub)\n", besiktas_as.show_info())
    print("----------------------------------------")
    print("(FootballClub)\n", besiktas_fc.show_info())