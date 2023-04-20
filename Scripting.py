
varList = []
with open('features.txt') as txtFile:
    lines = txtFile.readlines();
    for i in range(len(lines)):
        tempVal = lines[i].strip()
        tempVal = tempVal.replace(";","").split()
        if len(tempVal) > 1:
            print(tempVal)
            tempVal = tempVal[1]
            varList.append(tempVal)

txtFile.close

bltStr = "CREATE TABLE \"dataLog\" (\"uptime\" INTEGER DEFAULT 0,\"timeStamp\" INTEGER DEFAULT 0,\"sentToServer\" INTEGER DEFAULT 0,\"markToSent\" INTEGER DEFAULT 0 "
bltStr2 = "sql = \"INSERT INTO dataLog(uptime,timeStamp,sentToServer,markToSent"
for i in range(len(varList)):
    bltStr += "," + varList[i] + " REAL DEFAULT 0"
    bltStr2 += "," + varList[i]
bltStr += ");"
bltStr2 += ") VALUES(?"
for i in range(len(varList)+3):
    bltStr2 += ",?"
bltStr2 += ");\";"
txtFileW = open("CreateTable.txt", "w+")
txtFileW.write(bltStr)
txtFileW.close

txtFileW = open("InsertTable.txt", "w+")
txtFileW.write(bltStr2)
txtFileW.close

txtFileW = open("InsertBinder.txt", "w+")
txtFileW.write("    rc = sqlite3_bind_double(stmt, loc_count, current_sensor_data->uptime);\n")
txtFileW.write("    if (rc != SQLITE_OK)\n")
txtFileW.write("    {\n")
txtFileW.write("        error.lineNo = __LINE__;\n")
txtFileW.write("        error.rc = rc;\n")
txtFileW.write("        return error;\n")
txtFileW.write("    }\n")
txtFileW.write("    loc_count++;\n")
txtFileW.write("\n")
txtFileW.write("    rc = sqlite3_bind_int(stmt, loc_count, current_sensor_data->timestamp);\n")
txtFileW.write("    if (rc != SQLITE_OK)\n")
txtFileW.write("    {\n")
txtFileW.write("        error.lineNo = __LINE__;\n")
txtFileW.write("        error.rc = rc;\n")
txtFileW.write("        return error;\n")
txtFileW.write("    }\n")
txtFileW.write("    loc_count++;\n")
txtFileW.write("\n")
txtFileW.write("    rc = sqlite3_bind_int(stmt, loc_count, 0);\n")
txtFileW.write("    if (rc != SQLITE_OK)\n")
txtFileW.write("    {\n")
txtFileW.write("        error.lineNo = __LINE__;\n")
txtFileW.write("        error.rc = rc;\n")
txtFileW.write("        return error;\n")
txtFileW.write("    }\n")
txtFileW.write("    loc_count++;\n")
txtFileW.write("\n")
txtFileW.write("    rc = sqlite3_bind_int(stmt, loc_count, markToSent);\n")
txtFileW.write("    if (rc != SQLITE_OK)\n")
txtFileW.write("    {\n")
txtFileW.write("        error.lineNo = __LINE__;\n")
txtFileW.write("        error.rc = rc;\n")
txtFileW.write("        return error;\n")
txtFileW.write("    }\n")
txtFileW.write("    loc_count++;\n")
txtFileW.write("\n")
for i in range(len(varList)):
    txtFileW.write("    rc = sqlite_bind_double_status(stmt, loc_count, current_sensor_data->battery." + varList[i] +");\n")
    txtFileW.write("    if (rc != SQLITE_OK)\n")
    txtFileW.write("    {\n")
    txtFileW.write("        error.lineNo = __LINE__;\n")
    txtFileW.write("        error.rc = rc;\n")
    txtFileW.write("        return error;\n")
    txtFileW.write("    }\n")
    txtFileW.write("    loc_count++;\n")
    txtFileW.write("\n")
txtFileW.close

txtFileW = open("SQLFetch.txt", "w+")
txtFileW.write("        if(strcmp(azColName[i],\"uptime\") == 0)\n")
txtFileW.write("            fetched_sensor_data->uptime = atol(argv[i]);\n")
txtFileW.write("        else if(strcmp(azColName[i],\"timeStamp\") == 0)\n")
txtFileW.write("            fetched_sensor_data->timestamp = atol(argv[i]);\n")
txtFileW.write("        else if(strcmp(azColName[i],\"timeStamp\") == 0)\n")
txtFileW.write("            fetched_sensor_data->timestamp = atol(argv[i]);\n")
txtFileW.write("        else if(strcmp(azColName[i],\"system_mode\") == 0)\n")
txtFileW.write("        {\n")
txtFileW.write("            fetched_sensor_data->battery.system_mode = atoi(argv[i]);\n")
txtFileW.write("            printf(\"system_mode %lf\\r\\n\",fetched_sensor_data->battery.system_mode);\n")
txtFileW.write("        }\n")

for i in range(len(varList)):
    if varList[i] != "system_mode" and varList[i] != "sentToServer" and varList[i] != "markToSent" :
        txtFileW.write("        else if(strcmp(azColName[i],\"" + varList[i] +"\") == 0)\n")
        txtFileW.write("            fetched_sensor_data->battery." + varList[i] + " = atof(argv[i]);\n")
txtFileW.close

