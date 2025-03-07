class BaseClub:
    def __init__(self, club_name, **kwargs):
        self.club_name = club_name
        self.extras = kwargs
    
    def show_info(self):
        info = f"Club Name: {self.club_name}"
        for key, value in self.extras.items():
            info += f"\n{key.capitalize()}: {value}"
        return info


if __name__ == "__main__":
    besiktas = BaseClub("BesiktasJK", country="Turkey", founded_year=1903, colors="Black & White", fans_group="cArsi")
    print(besiktas.show_info())