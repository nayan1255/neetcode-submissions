class Solution:

    def encode(self, strs):
        res = ""
        for s in strs:
            # Prepends each string with its length and a '#' delimiter
            res = res + str(len(s)) + "#" + s
        return res
                                                                                                                                                                       
    """
    @param: str: A encoded single string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        res, i = [], 0
        
        while i < len(str):
            j = i
            # Find the delimiter that ends the length indicator
            while str[j] != "#":
                j += 1
            
            # Extract the length of the next string
            length = int(str[i:j])
            
            # Extract the actual string using the length and append to results
            original_string = str[j + 1 : j + 1 + length]
            res.append(original_string)
            
            # Move the pointer past the extracted string
            i = j + 1 + length
            
        return res
