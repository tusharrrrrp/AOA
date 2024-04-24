def rabin_karp(pattern,text):
    m,n=len(pattern),len(text)
    p,t=hash(pattern),hash(text[:m])
    result=[i for i in range(n-m+1) if hash(text[i:i+m])==p]
    return result
def hash(s):
    return sum(ord(c)for c in s )
if __name__=="__main__":
    text="AABAACAADAABAABA"
    pattern="AABA"
    print("Example:")
    print(rabin_karp(pattern,text))
