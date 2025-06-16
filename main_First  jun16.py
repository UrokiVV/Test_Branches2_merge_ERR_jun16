# main_First  jun16

print(" A1) Privet ! \n main_First")
print("Dev2) \nМы пишем, пишем, пишеи... ")
print("В далёкие края!")


def func2(x1):
    p = 4 * x1
    s = x1 * x1
    result = {"p": p, "s": s}
    return result


x = 5.0
res = func2(x)
print(f"\n x={x} : func2({x}) ==> p={res['p']:.3}, s={res['s']:.4}")
print("OK Dev2")
