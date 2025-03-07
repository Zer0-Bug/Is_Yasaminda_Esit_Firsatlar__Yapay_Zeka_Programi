class ClubStaff:
    def __init__(self, president_name, department_name_1, department_name_2):
        self.president_name = president_name
        self.__department_name_1 = department_name_1  # Private
        self.__department_name_2 = department_name_2  # Private
    
    def get_department_name_1(self):
        return self.__department_name_1
    
    def set_department_name_1(self, department_name_1):
        self.__department_name_1 = department_name_1

    def get_department_name_2(self):
        return self.__department_name_2
    
    def set_department_name_2(self, department_name_2):
        self.__department_name_2 = department_name_2

    def show_info(self):
        return f"President: {self.president_name}\nDepartment 1: {self.get_department_name_1()}\nDepartment 2: {self.get_department_name_2()}"



if __name__ == "__main__":
    besiktas_staff = ClubStaff("Serdar Adali", "Technical Department", "Scouting Department")
    print(besiktas_staff.show_info())
    besiktas_staff.set_department_name_1("Football Department")
    print("\nAfter updating Department 1:")
    print(besiktas_staff.show_info())