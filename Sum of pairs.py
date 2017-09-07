def sum_pairs(ints, s):
    num = set()       #使用set而不是用list，超级节省查找时间
    for i_v0 in ints:
        #i_v1 = s - i_v0
        #print(num)
        if s-i_v0 in num:
            return [s-i_v0,i_v0]
        num.add(i_v0)                  
    return None
