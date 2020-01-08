# read from file 

class inspector:
 
    def __init__(self,examinationNumber,errorRate,startFileCounter,usedPacket,cycle,numberOfSymbols):
        self.examinationNumber = examinationNumber
        self.errorRate=errorRate
        self.startFileCounter=startFileCounter
        self.usedPacket=usedPacket
        self.cycle=cycle
        self.numberOfSymbols=numberOfSymbols



def readFromFile():
    # test

    return 

def compareResult(AMCE,MDSE):
    counter = 0 
    for i in range(0,len(AMCE)):
        counter += MDSE[i].usedPacket - AMCE[i].usedPacket
    return counter

filePathAMC = 'AMC.txt'
filePathMDS = "MDS.txt"

AMCExamination = []
MDSExamination = []

with open(filePathAMC) as fp:
   for cnt, line in enumerate(fp):
        temp = line.split(":")
        tempInspector = inspector(int(temp[0]),int(temp[1]),int(temp[2]),int(temp[3]),int(temp[4]),int(temp[5]))
        AMCExamination.append(tempInspector)
        # print("Line {}: {}".format(cnt, line))

with open(filePathMDS) as fp:
   for cnt, line in enumerate(fp):
        temp = line.split(":")
        tempInspector = inspector(int(temp[0]),int(temp[1]),int(temp[2]),int(temp[3]),int(temp[4]),int(temp[5]))
        MDSExamination.append(tempInspector)

print(compareResult(AMCExamination,MDSExamination))