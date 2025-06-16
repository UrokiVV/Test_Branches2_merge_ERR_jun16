# main_First  jun16

print(" A1) Privet ! \n main_First")
print("Dev2) \nМы пишем, пишем, пишем... ")
print("В далёкие края!")
print("Для того, чтобы хорошо писать, надо писать.")
print("Чтобы хорошо программировать -  надо много программировать!.")

print(" A1) Вот и всё. \n  я звоню вам с вокзала.")
print("  Я спешу. \n  Извините меня!")


def func(x1):
    pi = 3.14
    p = pi * 2 * x1
    s = pi * x1 * x1
    result = {"p": p, "s": s}
    return result


x = 5
res = func(x)
print(f"\n x={x} : func({x}) ==> p={res['p']:.3}, s={res['s']:.4}")
print("OK master")


def func2(x1):
    p = 4 * x1
    s = x1 * x1
    result = {"p": p, "s": s}
    return result


x = 5.0
res = func2(x)
print(f"\n x={x} : func2({x}) ==> p={res['p']:.3}, s={res['s']:.4}")
print("OK Dev2")

