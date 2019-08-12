def grid_length(points):
    res=0
    for i in range(len(points)-1):
        horizontal_d=abs(points[i+1][0]-points[i][0])
        vertical_d=abs(points[i+1][1]-points[i][1])
        res+=max(horizontal_d,vertical_d)
    return res
