# main_First  jun16

print(" A1) Privet ! \n main_First")
print("Dev2) \nМы пишем, пишем, пишеи... ")
print("В далёкие края!")

def func(x1):
    p = 4 *x1
    s = x1 *x1
    res = {"p": p, "s": s}
    return res
x = 5.0
res = func(x)
print(f"\n x={x} : func({x}) ==> p={res['p']:.3}, s={res['s']:.4}")
print("OK Dev2")
