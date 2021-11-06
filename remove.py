def remove_outer_characters (a):
    a=a.replace(a[0], '', 1)
    a=a.replace(a[-1],'',1)
    print(a)

remove_outer_characters("String")
