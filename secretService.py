
class FBI:
    def __init__(self):#Instatiating the object class
        self._FBIVar = 0
    

obj = FBI()#calling the object
obj._FBIVar = "witness"
print(obj._FBIVar)

class CIA:
    def __init__(self):
        self.__secretVar = 13 #defining the variable

    def getSecret(self):
        print(self.__secretVar)

    def setSecret(self, secret):
        self.__secretVar = secret

obj = CIA() #calling the object
obj.getSecret()
obj.setSecret(24)
obj.getSecret()
