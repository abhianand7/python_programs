def sort_list(list_var):
    for i in range(0,len(list_var)):
        list_var[i] = ''.join(sorted(list_var[i]))
    list_var = sorted(list_var)
    print (list_var)







