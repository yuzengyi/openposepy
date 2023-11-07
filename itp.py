def getitp(y,c,threshold):
    if c[3]<= threshold or c[4]<= threshold or c[7]<= threshold or c[6]<= threshold:
        return 0
    elif y[4]<y[3] or y[7]<y[6]:
        #指示性姿态
        return 1
    else:
        #教师没有做指示性姿态
        return 0