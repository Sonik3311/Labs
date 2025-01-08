class Employee:
    def __init__(self, name="DefaultName", id=0, **kwargs):
        self.name = name
        self.id = id

    def get_info(self):
        return f"Id: {self.id}, name: {self.name}"

class Manager(Employee):
    def __init__(self, name="Manager", id=0, dep_id=0, **kwargs):
        super().__init__(name, id, **kwargs)
        self.dep_id = dep_id

    def get_info(self):
        return super().get_info() + f" Department: {self.dep_id}"

    def manage_project(self):
        print(self.get_info(), f"Managing project")

class Technician(Employee):
    def __init__(self, name="Technician", id=0, specialization="Job", **kwargs):
        super().__init__(name, id, **kwargs)
        self.specialization = specialization

    def get_info(self):
        return super().get_info() + f" Specialization: {self.specialization}"

    def perform_maintenance(self):
        print(self.get_info(), f"Performing maintenance as a {self.specialization}")

class TechManager(Manager, Technician):
    def __init__(self, name="TechManager", id=0, dep_id=0, specialization="TechManager"):
        super().__init__(name=name, id=id, dep_id=dep_id, specialization=specialization)
        self.employees = []

    def add_employee(self, employee:Employee):
        self.employees.append(employee)

    def get_team_info(self):
        print(self.get_info(), "Team composition:")
        for employee in self.employees:
            print("|" + employee.get_info())

tm = TechManager()
m = Manager(name="Manager0", id=1, dep_id=0)
tm.perform_maintenance()
tm.add_employee(m)
tm.add_employee(Employee(name="Employee2", id=2))
m.manage_project()
tm.get_team_info()
