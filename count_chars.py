
def count_chars(string):
    dic = {}
    for i in string:
        dic[i] = dic.get(i, 0) + 1
    print(dic)


count_chars("przyklad")
