def palindrome(string):
  text = ""
  reversed_text = ""

  for char in string:
    if char!=" ":
      text+=char.lower()

  

  for char in reversed(string):
    if char!=" ":
      reversed_text+=char.lower()
  

  return reversed_text==text
       


print(palindrome("No lemon no melon"))
print(palindrome("race car")) 
print(palindrome("hello"))   



