# This is a Function to find frequency of a char in a strning using hashing

# Psuedo Code:
"""
S = 'adgkjlaasda'
char = 'a'

char_freq(S, char):
    hash = [0]*26    // Initialize a list of size 26 with 0
    for c in S:
        hash[S[c]-a]++
    
    return hash[char-a]
"""

# implementation :

def char_freq(strn,char):
    hash=[0]*26
    for c in strn:
        hash[ord(c)-ord('a')] +=1
    return hash[ord(char)-ord('a')]

S = "adgkjlaasda"
char = "a"
count = char_freq(S,char)
print(f"The character '{char}' occurs {count} in the string: '{S}'")


# T.C = O(n)  where n is size of the string
# S.C = O(1) as size remains constant of 26.