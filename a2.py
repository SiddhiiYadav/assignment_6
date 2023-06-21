def ds(a=1,b="default"):
    print(" 1)Normal\n 2)List \n 3)Tuple\n 4)Set\n 5)Dictionary")
    i=int(input("Enter type 0f datastructure"))
    if i==1:
        return a,b
    elif i==2:    
        print("Choose: 1) create 2) update 3) del")
        if 
        list=[a,b]
        return list
    elif i==3:
        tuple=(a,b)
        return tuple
    elif i==4:
        set={a,b}
        return set
    elif i==5:
        dictionary={
            "roll no":a,
            "name":b
            }
        return dictionary
    if i==1:
        del(a,b)
        print(a,b)
    elif i==2:
        del list
        print(list)
    elif i==3:
        del(tuple)
        print(tuple)
    elif i==4:
        del(set)
        print(set)
    elif i==5:
        del(dictionary)
        print(dictionary)
print(ds(102,"shubham"))