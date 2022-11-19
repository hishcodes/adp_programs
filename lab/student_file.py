import shelve

f = open("student.txt", "w")

f.write("USN \t NAME \t\t MARKS\n")
f.write("101 \t Hisham \t 90\n")
f.write("102 \t Moideen \t 80\n")

f = open("student.txt")
r = f.read()
print(r)
f.close()