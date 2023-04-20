
varList = []
with open('features.txt') as txtFile:
    lines = txtFile.readlines();
    for i in range(len(lines)):
        tempVal = lines[i].strip()
        tempVal = tempVal.replace(";","").split(" ")
        print(tempVal)
        if len(tempVal) > 1:
            tempVal = tempVal[1]
            varList.append(tempVal)

bltStr = "CREATE TABLE \"dataLog\" (\"uptime\" INTEGER DEFAULT 0, \"timeStamp\" INTEGER DEFAULT 0, \"sentToServer\" INTEGER DEFAULT 0, \"markToSent\" INTEGER DEFAULT 0 "
bltStr2 = "INSERT INTO dataLog(uptime,timeStamp"
for i in range(len(varList)):
    bltStr += "," + varList[i] + " REAL DEAFAULT 0"
    bltStr2 += "," + varList[i]
bltStr += ");"
bltStr2 += ") VALUES(?"
for i in range(len(varList)+1):
    bltStr2 += ",?"
bltStr2 += ")"
txtFileW = open("CreateTable.txt", "w+")
txtFileW.write(bltStr)

txtFileW = open("InsertTable.txt", "w+")
txtFileW.write(bltStr2)

