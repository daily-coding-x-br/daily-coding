def sol(w,s):
    if len(s)<len(w):
        return []
    w_count={}
    s_count={}
    total_count=len(w)
    res=[]
    
    for l in w:
        if l not in w_count:
            w_count[l]=1
        else:
            w_count[l]+=1
    for l in s[:len(w)]:
        if l not in s_count:
            s_count[l]=1
        else:
            s_count[l]+=1
        if l in w_count and w_count[l]>=s_count[l]:
            total_count-=1
    if total_count==0:
        res.append(0)
    for i in range(1,len(s)-len(w)+1):
        out_letter=s[i-1]
        in_letter=s[i+len(w)-1]
        s_count[out_letter]-=1
        if out_letter in w_count and s_count[out_letter]<w_count[out_letter]:
            total_count+=1
        if in_letter not in s_count:
            s_count[in_letter]=1
        else:
            s_count[in_letter]+=1
        if in_letter in w_count and s_count[in_letter]<=w_count[in_letter]:
            total_count-=1
        if total_count==0:
            res.append(i)
    return res
            
            