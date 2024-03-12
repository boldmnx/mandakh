s = [7, 6, 5, 4, 3, 2, 1]


def swap(s):
    ordList = []
    # left=[]
    # right=[]
    l1=0
    while len(s) > 1:
        left = s[:len(s)//2]
        right = s[len(s)//2:]
        if len(left) < 2:
            return swap(right)
        elif len(right) < 2:
            
            return swap(left)
        if len(left)==1 and len(right)==1:
            if left[0]>right[0]:
                ordList.append(right[0])
        # if len
        # while len(right) > 1:
        #     return swap(right)
        return swap(left)
    if left > right:
        pass


# divide
# conque
# combine
swap(s)
