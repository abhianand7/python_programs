import collections

def isPalindrome(s):
    return s.lower() == s[::-1].lower()

def anagramchk(word,chkword):
    return sorted(word.lower()) == sorted(chkword.lower())

def allAnagrams(dictfilepath):
    answer = collections.defaultdict(list)
    with open(dictfilepath) as dictfile:
        for line in dictfile:
            word = line.strip().lower()
            answer[''.join(sorted(word))].append(word)
    return answer

def fetchAllAnagrams(wordin, anagrams):
    return anagrams[''.join(sorted(wordin.lower()))]

def main(dictfilepath, palsfilepath):
    anagrams = allAnagrams(dictfilepath)
    with open(palsfilepath) as palfile:
        for line in palfile:
            word = line.strip().lower()
            if isPalindrome(word):
                for anagram in anagrams[''.join(sorted(word))]:
                    if isPalindrome(anagram):
                        print ("%s is an anagram of %s" %(anagram, word))