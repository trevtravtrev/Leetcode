# LEETCODE PREMIUM PROBLEM - https://www.lintcode.com/problem/659/
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        encoded = ""
        for str in strs:
            for char in str:
                # replace : with :: so we can distinguish a : from our separator
                if char == ":":
                    encoded+="::"
                else:
                    encoded+=char
            # :; is word separator
            encoded+=":;"
        return encoded

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        decoded = []
        word = []
        i = 0
        while (i < len(str)):
            # if char is actual : or separator :
            if str[i] == ":":
                # if char is separator :
                if str[i+1] == ";":
                    # add previous word before separator detected to decoded list
                    decoded.append("".join(word))
                    # reset previous word
                    word = []
                    # jump over the separator to next char
                    i+=2
                # if char is actual :
                else:
                    # add actual : to decoded
                    decoded.append(":")
                    # jump over the ::
                    i+=2
            # if regular char
            else:
                # append char to word
                word.append(str[i])
                i+=1
        return decoded