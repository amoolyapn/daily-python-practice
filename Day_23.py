#Dictionary
student={
    "name":"Ammu",
    "age":23,
    "city":"Blr"
}

student["age"]=21
student["Grade"]=8.7
for key,value in student.items():
    print(key,":",value)


#Palindrome
class Solution:
    def isPalindrome(self,x):
        if x<0:
            return False
        original = x
        reversed = 0
        while x>0:
            digit = x%10
            reversed = reversed*10+digit
            x = x//10
        return original = reersed
sol = Solution()
num=int(input("Enter the value:"))
if sol.isPalindrome(num):
    print("Palindrome")
else:
    print("Not Palindrome")


#Panagrams
def is_pangram(sentence):
    sentence = sentence.lower() 
    letters = set()            

    for char in sentence:
        if 'a' <= char <= 'z':   
            letters.add(char)

    if len(letters) == 26:
        return "Pangram"
    else:
        return "Not a Pangram"
text = input("Enter a sentence: ")
print(is_pangram(text))



#Anagrams
def anagram(w1,w2):
    w1 = w1.replace(" ", "").lower()
    w2 = w2.replace(" ","").lower()
    return sorted(w1) == sorted(w2)
w1=input("Enter w1: ")
w2=input("Enter w2: ")
print(anagram(w1,w2))

            
