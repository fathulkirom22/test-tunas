import copy

def tingkat_kemahiran_max(NM, Ai, Bi):
    res = NM[1]
    TMP_Ai = copy.deepcopy(Ai)
    for i in range(0, NM[0]):
        kemahiran_musuh = min(TMP_Ai)
        if kemahiran_musuh <= res:
            TMP_Ai.remove(kemahiran_musuh)
            res = res + Bi[Ai.index(kemahiran_musuh)]
    return res
        

res = tingkat_kemahiran_max([4,2], [8,9,3,2], [5,4,1,3])
res1 = tingkat_kemahiran_max([5,3], [8,4,5,6,7], [9,8,7,5,6])
res2 = tingkat_kemahiran_max([5,9], [2,3,6,7,8], [3,4,2,2,3])
print("res", res)
print("res", res1)
print("res", res2)