class ClubStaff:
    def __init__(self, president_name):
        self.president_name = president_name

    def show_department_info(self):
        return f"President: {self.president_name}"


class TechnicalTeam(ClubStaff):
    def __init__(self, president_name, technic_director):
        super().__init__(president_name)
        self.technic_director = technic_director

    def show_department_info(self):
        return f"Technical Director: {self.technic_director}"


class ScoutTeam(ClubStaff):
    def __init__(self, president_name, chef_scout):
        super().__init__(president_name)
        self.chef_scout = chef_scout

    def show_department_info(self):
        return f"Chief Scout: {self.chef_scout}"



if __name__ == "__main__":
    staff = ClubStaff("Serdar Adali")
    tech = TechnicalTeam("Serdar Adali", "Ole Gunnar Solskjaer")
    scout = ScoutTeam("Serdar Adali", "Eduard Graf")
    print(staff.show_department_info())
    print(tech.show_department_info())
    print(scout.show_department_info())