def sol(s,letters):
    L=len(s)
    letters=set(letters)
    N=len(letters) #O(n)
    m=-1
    chars=set(s[:N])&letters
    i,im=0,0
    j=N
        
    while i<L-N+1:
        first_t=True
        while j<L or first_t:
            first_t=False
            if len(chars)==N:
                if (j-i<m) or m==-1:
                    m=j-i
                    im=i
                break
            if j<L:
                if s[j] in letters:
                    chars.add(s[j])
                j+=1
        if s[i] in chars and not s[i] in s[i+1:j]:
            chars.remove(s[i])
        print(i,j,s[im:im+m])
        i+=1
    if letters-set(s[im:im+m]):
        return None
    return s[im:im+m]
        
        
    
