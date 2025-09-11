class Cricket:
    teamN = 'India'
    def __init__(self,jn,n,r,w):
        self.jersey = jn
        self.name = n
        self.run = r
        self.wicket = w
        
    
    def setJerseyno(self, nj):
        self.jersey  = nj
    def getJerseyno(self):
        return self.jersey
    
    def setName(self,nn):
        self.name = nn
    def getName(self):
        return self.name
    
    def setRuns(self,nr):
        self.run = nr
    def getRuns(self):
        return self.run
    
    def setWicket(self,nw):
        self.wicket = nw
    def getWicket(self):
        return self.wicket
        
s1 = Cricket(5,'virat ',5,2)
# print(s1.name)
print(s1.teamN)
s1.setJerseyno(6)
print(s1.getJerseyno())

s1.setName('Virat Kohli')
print(s1.getName())

s1.setRuns(11)
print(s1.getRuns())

s1.setWicket(3)
print(s1.getWicket())
