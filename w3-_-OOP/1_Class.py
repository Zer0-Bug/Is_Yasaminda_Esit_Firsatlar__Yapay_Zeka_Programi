class BaseClub:
    def __init__(self, club_name, country, founded_year, colors, fans_group):
        self.club_name = club_name
        self.country = country
        self.founded_year = founded_year
        self.colors = colors
        self.fans_group = fans_group
    
    def show_info(self):
        return f"Club Name: {self.club_name}\nCountry: {self.country}\nFounded Year: {self.founded_year}\nColors: {self.colors}\nFan Group: {self.fans_group}"


if __name__ == "__main__":
    besiktas = BaseClub("BesiktasJK", "Turkey", 1903, "Black & White", "cArsi")
    print(besiktas.show_info())