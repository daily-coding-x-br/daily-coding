class Interval:
    def __init__(self,a,b):
        self.a=a
        self.b=b
def intersec(x,y):
    if x.b<y.a or y.b<x.a:
        return None
    return Interval(max((x.a,y.a)),min((x.b,y.b)))

def sol(list_itv):
    intersec_list=[]
    for aux in list_itv:
        it=Interval(*aux)
        check=False
        for idx in range(len(intersec_list)):
            aux_itv=intersec(it,intersec_list[idx])
            if aux_itv:
                intersec_list[idx]=aux_itv
                check=True
        if not check:
            intersec_list.append(it)
    return [t.a for t in intersec_list]