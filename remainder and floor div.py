import decimal
import decimal
a = int(input("Enter a number: "))
b = int(input("Enter the base to convert to: "))


def dec_to_base_b(a, b):

    print("\n")

    list = []
    while a >= 1:   
        print(a, "|", a//b, "|", a%b)
        list.append(a%b)
        a = a//b

    print("\n")
    def swap(list):
        list.reverse()
        return list
    
    for i in swap(list):
        if i >= 10 and b == 16:
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


dec_to_base_b(a, b)