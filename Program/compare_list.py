
a = [3,5,7,8,9]
b = [3,5,7,8,9]
# b = [4,7,1,5,9,3]


if (len(a) != len(b)):
    print ("List are not equel")
else:
    for i in range(len(a)):
        if a[i] != b[i]:
            print("Not Equel")
            break
    else:
        print("Both String are equel")