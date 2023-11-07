def getdtp(y,c,threshold):
    if c[3]<= threshold or c[4]<= threshold or c[7]<= threshold or c[6]<= threshold:
        return 0
    elif y[4]<y[3] and y[7]<y[6]:
        #上区手势
        return 1
    else:
        #教师没有做上区手势
        return 0