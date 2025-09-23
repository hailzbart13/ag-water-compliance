#Water Regulation Compliance Checker
#This program reads farm water usage from a file and reports weather each farm is Compliant or in Violation based on the 4.0 acre-feet per acre regulation.
file=input("Enter File Name:")
file1=open(file)
compliant=0
violations=0
for line in file1:
    line=line.split()
    farm=line[0]
    usage=float(line[1])
    if usage<=4.0:
        print(farm, "Compliant")
        compliant+=1
    else:
        print(farm, "Violation")
        violations+=1
print("Summary")
print("Compliant farms:", compliant)
print("Violations:", violations)