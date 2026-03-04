class SiblingA:
    def feature_a(self):
        print("Feature from Sibling A")

class SiblingB:
    def __init__(self):
        self.helper = SiblingA() 

    def feature_b(self):
        print("Feature from Sibling B calling...")
        self.helper.feature_a() 

obj = SiblingB()
obj.feature_b()