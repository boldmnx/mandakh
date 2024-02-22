class HospitalCass:
    # Queque is FIFO
    def __init__(self):
        self.__oochir = []

    def first(self):
        return print(self.__oochir[0])

    def tasalbar_avah(self, tasalbar):
        self.__oochir += [tasalbar]

    def tasalbar_uguh(self):
        if self.__oochir:
            tasalbar = self.__oochir[0]
            self.__oochir = self.__oochir[1:]
            return tasalbar
        return 'error'





        

    def len(self):
        count = 0
        for i in self.__oochir:
            count += 1
        return count

    def is_empty(self):
        return self.len() == 0

    def get_hospital_cass(self):
        return print(self.__oochir)

# function dtor yum bichij bolohgui uchir n len print bichheer isempty ajilluulhad hevlej gargaj irj bna ingej bolohgui


hospital = HospitalCass()

# hospital.tasalbar_avah(5)
# hospital.get_hospital_cass()

# hospital.tasalbar_avah(3)
# hospital.get_hospital_cass()
# print(hospital.len())
# print(hospital.tasalbar_uguh())
# print(hospital.is_empty())
# print(hospital.tasalbar_uguh())
# print(hospital.is_empty())
# print(hospital.tasalbar_uguh())
# hospital.tasalbar_avah(7)
# hospital.get_hospital_cass()
# hospital.tasalbar_avah(9)
# hospital.get_hospital_cass()
# hospital.first()
# hospital.tasalbar_avah(4)
# hospital.get_hospital_cass()
# print(hospital.len())
# print(hospital.tasalbar_uguh())


# hospital.tasalbar_avah(1)
# hospital.tasalbar_avah(4)
# hospital.tasalbar_avah(10)


# hospital.get_hospital_cass()
# print(hospital.len())

# hospital.tasalbar_uguh()
# hospital.get_hospital_cass()

# print(hospital.len())
# print(hospital.is_empty())
