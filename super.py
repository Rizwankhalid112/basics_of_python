class Phone:

    def call(self):

        print("Connecting to network...")

class SmartPhone(Phone):

    def call(self):

        Phone.call(self) 

        print("Starting Video Stream...")


iphone = SmartPhone()
iphone.call()

