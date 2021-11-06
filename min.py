minlist=[34,21,90,14]
def find_min(array):
    array.sort()
    print("Minimum value is  : ", array.pop(0) )


find_min(minlist)
