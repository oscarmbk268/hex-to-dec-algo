a = int(input("Enter a number: "))
print("\n")

list = []
while a >= 1:   
    print(a, "|", a//16, "|", a%16)
    list.append(a%16)
    a = a//16

print("\n")
def swap(list):
    list.reverse()
    return list
    
for i in swap(list):
    if i >= 10:
        i = str(i)
        if i == "10":
            i = "A"
        elif i == "11":
            i = "B"
        elif i == "12":
            i = "C"
        elif i == "13":
            i = "D"
        elif i == "14":
            i = "E"
        elif i == "15":
            i = "F"
    print(i, end="")
