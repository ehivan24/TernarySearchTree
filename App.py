__author__ = 'edwingsantos'


from TernarySearchTree.TST import TST

tst = TST()

tst.put("apple", 100)
tst.put("orage", 200)
tst.put("appio", 120)



print(tst.get("apple"))
print(tst.get("appble"))
print(tst.get("appio"))
print(tst.get("apples"))