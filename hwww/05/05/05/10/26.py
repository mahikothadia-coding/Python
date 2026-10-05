from abc import ABC, abstractmethod
 
class Smartdevice(ABC):

 
    def show_device(self, name):
        print("Device name:", name)
 
   
    @abstractmethod
    def turn_on(self):
        pass
 
 

class Smartlight(Smartdevice):
    def turn_on(self):
        print("Smart light is  on.")
 
 
class Smartfan(Smartdevice):
    def turn_on(self):
        print("Smart fan is  on.")
 
 
class Smartspeaker(Smartdevice):
    def turn_on(self):
        print("Smart speaker is  on.")
 
 

light = Smartlight()
fan = Smartfan()
speaker = Smartspeaker()
 
light.show_device("Living room light.")
light.turn_on()
 
fan.show_device("Bedroom fan.")
fan.turn_on()
 
speaker.show_device("Music speaker.")
speaker.turn_on()
 
 
 
class Securitycamera:
    def check_status(self):
        print("Security camera is recording.")
 
 
class Doorlock:
    def check_status(self):
        print("Door lock is secure.")
 

 
devices = [Securitycamera(), Doorlock()]
 
print("")
print("=== SMART DEVICE STATUS ===")
 
for device in devices:
    device.check_status()
 
