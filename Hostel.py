class Hostel:
    
    hostel_fee = 5000 

    def __init__(self, sn, rn):
        self.studentName = sn
        self.roomNumber = rn
        
    def setSName(self,snn):
        self.studentName = snn
    def getSName(self):
        return self.studentName
    
    def setRooN(self,nr):
        self.roomNumber = nr
    def getRoomN(self):
        return self.roomNumber
    @classmethod
    def setHostelF(cls,newf):
        cls.hostel_fee=newf
    @classmethod
    def getHostelF(cls):
        return cls.hostel_fee

s1 = Hostel("Tejaswini ", 101)
s1.setSName("Tejaswini Kshirsagar")
print(s1.getSName())

s1.setRooN(102)
print(s1.getRoomN())

s1.setHostelF(6000)
print(s1.getHostelF())
