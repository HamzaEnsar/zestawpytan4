minlist=[34,21,90,14]
def min_max(array):
    array.sort()
    print("Küçük : ", array.pop(0), "büyük : ", array.pop(-1))


min_max(minlist)