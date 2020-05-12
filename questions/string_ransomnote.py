# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines
# otherwise, it will return false.
# Each letter in the magazine string can only be used once in your ransom note.
# Note:
# You may assume that both strings contain only lowercase letters.

# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

def can_construct(note, magazine):

    for char in note:
        if magazine.count(char) < note.count(char):
            return False
    
    return True


# SYS OUT
print(can_construct("a", "b"))