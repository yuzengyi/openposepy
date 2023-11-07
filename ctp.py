def getctp(x,c,threshold):
    random1=0.2
    random_1=0.2
    if c[0]<= threshold or c[17]<= threshold or c[18]<= threshold:
        return 0
    elif (x[0]-x[17])-(x[18]-x[0])>random1*(x[0]-x[17]):
        #教师往他/她的左侧看
        return 1
    elif (x[18]-x[0])-(x[0]-x[17])>random_1*(x[18]-x[0]):
        #教师往他/她的右侧看
        return -1
    else:
        #教师看中间
        return 0