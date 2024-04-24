#def search_pattern(pattern, text):
#    # Get the lengths of the pattern and the text
#    m = len(pattern)
#    n = len(text)
#
#    # A loop to slide pattern over text one by one
#    for i in range(n - m + 1):
#        # For current index i, check for pattern match
#        j = 0
#        while j < m and text[i + j] == pattern[j]:
#            j += 1
#
#        # If the entire pattern matches the text starting at index i
#        if j == m:
#            print(f"Pattern found at index {i}")
#
#
## Example usage
#if __name__ == "__main__":
#    # Example 1
#    text1 = "AABAACAADAABAABA"
#    pattern1 = "AABA"
#    print("Example 1:")
#    search_pattern(pattern1, text1)
#
#    # Example 2
#    text2 = "agd"
#    pattern2 = "g"
#    print("\nExample 2:")
#    search_pattern(pattern2, text2)
def search_position(pattern,text):
    m=len(pattern)
    n=len(text)
    for i in range(n - m + 1):
        j=0
        while j<m and text[i+j]==pattern[j]:
            j+=1
        if j==m:
            print(f"pattern found at index{i}")

if __name__=="__main__":
    text1="AABAA"
    pattern1="AABA"
    print("example1:")
    search_position(pattern1,text1)

    text2 = "agd"
    pattern2 = "g"
    print("\nExample 2:")
    search_position(pattern2, text2)