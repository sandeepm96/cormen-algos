#passed the finishing time as sorting parameter
def getkey(item):
    return item[1]
def activitySelection(activityArray):
    n = len(activityArray)
    selected = []
    i = 0
    selected.append(activityArray[i])
    for j in range(len(activityArray)):
        if activityArray[j][0]>=activityArray[i][1]:
            selected.append(activityArray[j])
            i = j
    return selected

if __name__ == "__main__":
    s = list(map(int,input().split()))
    f = list(map(int,input().split()))
    act_name = list(range(len(s)))
    activityarr = list(zip(s,f,act_name))
    #sorted by finishing time
    activityarr = sorted(activityarr,key = getkey)
    activityorder = activitySelection(activityarr)
    for i in range(len(activityorder)):
        print(activityorder[i][2])