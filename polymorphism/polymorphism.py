class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language in India.")

    def type(self):
        print("India is a developing country.")

class China():
    def capital(self):      
        print("The capital of China is Beijing.")

    def language(self):
        print("The most widely spoken langauge in China is chinese") 

    def type(self):
        print("China is a developed country.")

obj_ind = India()
obj_chi = China()

for country in (obj_ind, obj_chi):
    country.capital()
    country.language()
    country.type()