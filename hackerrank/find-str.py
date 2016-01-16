 
super_string = input()
sub_string = input()
if len(sub_string) == 1:
    print (super_string.count(sub_string))
else:
    sub_str_len = len(sub_string)
    count = 0
    for i in range(super_string.index(sub_string),len(super_string) - 1):
        if super_string[i:sub_str_len+i] == sub_string:
            count +=1
    print (count)
            