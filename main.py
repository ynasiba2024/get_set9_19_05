#6-masala
class Hospital:
    def __init__(self, hospital_name, patients):
        self.hospital_name = hospital_name
        self.__patients = patients

    def get_patients(self):
        return self.__patients

    def set_patients(self, new_patients):
        if new_patients > self.__patients:
            self.__patients = new_patients
            print("Bemorlar soni yangilandi")
        else:
            print("Bemorlar soni kamaymasligi kerak")


h1 = Hospital("Shifo Med", 200)

print(h1.get_patients())

h1.set_patients(250)
print(h1.get_patients())

h1.set_patients(150)
