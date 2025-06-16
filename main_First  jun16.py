# main_First  jun16

print(" A1) Privet ! \n main_First")
print("Dev2) \nМы пишем, пишем, пишеи... ")
print("В далёкие края!")

print("Для того, чтобы хорошо писать, надо писать.")
print("Чтобы хорошо программировать -  надо много программировать!.")

print(" A1) Вот и всё. \n  я звоню вам с вокзала.")
print("  Я спешу. \n  Извините меня!")

def func(x1):
    pi = 3.14
    p = pi *2 *x1
    s = pi * x1 *x1
    res = {"p": p, "s": s}
    return res
x = 5
res = func(x)
print(f"x={x} : func({x}) ==> p={res['p']:.3}, s={res['s']:.4}")
print("OK master")


