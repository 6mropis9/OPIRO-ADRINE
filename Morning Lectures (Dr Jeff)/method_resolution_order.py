class SmartDevice:
    def info(self):
        print("SmartDevice basic info")

class Phone(SmartDevice):
    def info(self):
        print("Phone: can make calls")

class Camera(SmartDevice):
    def info(self):
        print("Camera: can take photos")

class SmartPhone(Phone, Camera):
    pass

# Test
device = SmartPhone()
device.info()  # Output: Phone: can make calls

# Show MRO
print(SmartPhone.__mro__)