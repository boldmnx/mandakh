class Doctorr:
    def __init__(self):
        self.__currentPerson = "" 
        self.__healed = [] 

    def setter_healed(self, name):
        self.__healed += [name] 
    
    def getter_healed(self):
        return self.__healed 

    def setter_currentPerson(self, name):
        self.__currentPerson = name 
    
    def getter_currentPerson(self):
        return self.__currentPerson
