class Name():
    def __init__(self, first_name, last_name):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.full_name = f"{self.first_name} {self.last_name}"
        self.initials = f"{self.first_name[0]}.{self.last_name[0]}"


a = Name('john', 'sMiTH')
print(a.first_name)
print(a.last_name)
print(a.full_name)
print(a.initials)
