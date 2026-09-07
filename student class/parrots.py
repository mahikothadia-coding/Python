class Parrot:
    species = "bird"

    def __init__(self, name,age):
        self.name = name
        self.age = age

woo = Parrot("woo",10)
roo = Parrot("roo", 12)

print(woo.species)
print(roo.species)
print(woo.name)
print(roo.name)
print(woo.age)
print(roo.age)
