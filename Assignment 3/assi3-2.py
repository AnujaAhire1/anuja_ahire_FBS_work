#WAP to input any alphabet and check whether it is vowel or consonant.

ch = input('Enter an alphabet: ') 

if ch in ' aeiouAEIOU':
    print('It is a Vowel.')
else:
    print('It is a Consonant.')
