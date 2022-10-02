class EmployeeDetails:
    __name = ""
    __monthlySalary = 0.0
    __age = 0
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def monthlySalary(self):
        return self.__monthlySalary

    @monthlySalary.setter
    def monthlySalary(self, monthlySalary):
        self.__monthlySalary = monthlySalary

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age