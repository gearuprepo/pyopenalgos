# Given a sentence, reverse each word in the sentence while keeping the order the same!
# Code 

def word_flipper(our_string):

    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """
    
    split = our_string.split(" ")
    retval = []
    for s in split:
        retval.append(s[::-1])
    retvalstr =  " ".join(retval)
    return retvalstr
# Test Cases
print ("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print ("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
print ("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")