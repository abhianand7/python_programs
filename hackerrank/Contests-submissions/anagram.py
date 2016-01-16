 
w1=raw_input()
w2=raw_input()

total=0
for letter in "abcdefghijklmnopqrstuvwxyz":
    x = abs(w1.count(letter) - w2.count(letter))
    total+= x
print total
