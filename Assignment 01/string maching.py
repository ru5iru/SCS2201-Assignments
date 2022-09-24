#linecache package helps to access specific lines in a file
import linecache

def kmp(pattern, text):
    M = len(pattern)        # Length of the pattern
    N = len(text)           # Length of the text
    matchCount = 0          # Number of matches
    lineCount = 1           # Number of lines passed
    
    # Create lps array (Pi array)
    lps = [0] * M
    j = 0
    
    length = 0              # Length of the previous longest prefix suffix
    
    i = 1                   # lps array calculated from index 1, lps[0] is always 0
    while i < M:            # Calculates Pi values for each character
        if pattern[i] == pattern[length]:
            length += 1                     # When characters are matched,
            lps[i] = length                 # length incremented by 1 and it assigns to lps array
            i += 1                          # i is incremented by 1
        
        elif length == 0:                   # When lps length is zero and characters are not matching,
            lps[i] = 0                      # lps value should be 0
            i += 1                          # i is incremented by 1
        
        else:
            length = lps[length - 1]        # When length is not zero, previous index's value asigned to length 
    
    i = 0                       # Index for text
    while i < N:
        if text[i] == '\n':             # When newline character is found,
            lineCount += 1              # lineCount is incremented by 1
        
        if pattern[j] == text[i]:
            i += 1                      # When a matching character is found 
            j += 1                      # Both i and j are incremented by 1
        
        if j == M:                  # j = M means matching string is found
            j = lps[j-1]
            content = linecache.getline('modules.txt', lineCount)       # Access the line
            print(content, end = '')                                    # Outputs the line
            matchCount += 1                     # Number of matches is incremented by 1
        
        elif i < N and pattern[j] != text[i]:   # Not the end of the text and characters are not matched
            if j == 0:                          # if index of the pattern is 0
                i += 1                          # Moves to the next character
            else:
                j = lps[j-1]                    # Pattern index sets to lps value of previous character
    
    print("Number of matches: ", matchCount)        # Outputs the Number of matches found
    
    
f = open("modules.txt", "r")                    # Opens the file

fileContent = f.read()                          # Reads the file content
searchString = input("Enter a search string: ")     # Gets the search string as a input

pattern = searchString.lower()          # Convert both text and pattern to lowercase because,
text = fileContent.lower()              # String matching should be case-insensitive

kmp(pattern, text)    