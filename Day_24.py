#Counting the vowels in a given string
s = "Amoolya"
s1 = "Education"
s2 = "Element"
vowels = "aeiou"
s3= s.lower()
s4 = s1.lower()
s5 = s2.lower()
count = sum(1 for ch in s3 if ch in vowels)
print(count)
count1 = sum(1 for ch in s4 if ch in vowels)
print(count1)
count2 = sum(1 for ch in s5 if ch in vowels)
print(count2)


#2
s = "Amoolya"
s1 = "Education"
s2 = "Element"
vowels = "aeiou"
count = sum(1 for ch in s.lower() if ch in vowels)
print(count)
count1 = sum(1 for ch in s1.lower() if ch in vowels)
print(count1)
count2 = sum(1 for ch in s2.lower() if ch in vowels)
print(count2)


#Replacing spaces with dashes
a=" a m ooly a"
print(a.replace(" ","_"))


#Checking 2 strings are Anagrams
def anagram(word1,word2):
   return sorted(word1)==sorted(word2)
      
word1 = input("Enter word1: ")
word2 = input("Enter word2: ")

if anagram(word1,word2):
    print("Is Anagram")
else:
    print("Is Not Anagram")


#Reverse words in a sentence

#Split() - method
n = input("Enter a value").split()
print(n)


#1
def reverse(a):
    return a[::-1]
a= input("Enter a value: ")
print("Reversed: ",reverse(a))


#2
s = "hello world"
words = s.split()
reversed_sentence = ''.join(reversed(words))
print(reversed_sentence)  #world hello


#3
s = "hello world"
words = s.split()
reversed_each_word = [word[::-1] for word in words]
result = ' '.join(reversed_each_word)
print(result)   #olleh dlrow


#Find first non-repeating character
def first_non_repeating_char(s):
    for ch in s:
        if s.count(ch) == 1:
            return ch
    return "None"

s = input("Enter a string: ")
result = first_non_repeating_char(s)
print("First non-repeating character:", result)
