d = {"Hisham":{"P":100, "C":80, "M":90}, "Aditya":{"P":80, "C":90, "M":100}, "Fahad":{"P":90, "C":100, "M":80}}

print('Name\t\tPhysics\t\tChemistry\tMaths')
for key,value in d.items():
    print(str(key) +"\t\t"+ str(d[key]["P"]) +"\t\t"+ str(d[key]["C"]) +"\t\t"+ str(d[key]["M"]))