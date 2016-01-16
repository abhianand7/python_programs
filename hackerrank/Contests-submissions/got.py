 
s = raw_input()
count = {}
for i in range(len(s)):
    if s[i] not in count: count[s[i]] = 0
    count[s[i]] += 1
isPalindrome = True
hasOdd = False
for k in count :
    k = len(k)
    break
if (k % 2 != 0): hasOdd = True
for k in count:
    if count[k] % 2 != 0:
        if hasOdd: hasOdd = False
        else:
            isPalindrome = False
            break
print "YES" if isPalindrome else "NO"
