# ====================================
'''
https://www.youtube.com/watch?v=jXugs4B3lwU
key takeaway points:

Lookups happen at runtime
Locations decided at compile time
'''
# ====================================
# return x as global x
# x = "global x"
# def level_one():
#     return x
# level_one()
# ====================================
# return x as local x, even if condition not satisfied, global x is ignored
# x = "global x"
# def level_two(v):
#     print(v)
#     if v:
#         x = "local x"
#     return x
# level_two(True) # or False
# ====================================
# x = "global x"
# def level_three():
#     z = "outer z"
#     def inner(y):
#         return x, y, z
#     return inner("y arg")
# print(level_three())
# ====================================
# whether z is defined before inner() or not, won't matter
# at compile time z is decided as "outer z" but not defined, when return inner() happen at runtime, z is then defined
# x = "global x"
# def level_three():
#     def inner(y):
#         return x, y, z
#     z = "outer z"
#     return inner("y arg")
# print(level_three())
# ====================================
# x = "global x"
# def leve_four():
#     z = "first outer z"
#     def inner(y):
#         return x, y, z
#     z = "second outer z"  # second z is used, rather then the first z
#     return inner("y arg")
# print(leve_four())
# ====================================
# Closures
# x = "global x"
# def leve_four():
#     z = "first outer z"
#     def inner(y):
#         return x, y, z
#     print(inner.__closure__)
#     z = "second outer z"
#     print(inner.__closure__)
#     return inner("y arg")
# print(leve_four())
# ====================================
# x = "globa x"
# def leve_five(n):
#     z = f'outer z {n}'
#     def inner(y):
#         return x, y, z
#     return inner
# def main():
#     f = leve_five(0)
#     g = leve_five(1)
#     print(f("y arg"), g("outer y arg"))
# main()
# ====================================
# x = "global x"
# def level_six():
#     z = "outer z"
#     def donky():
#         def inner(y):
#             return x, y, z   # x location is decided here
#         z = "donky z"
#         return inner         # z is defined here
#     def chonky():
#         x = "chonky x"
#         f = donky()
#         return f("y arg")
#     return chonky()
# print(level_six())
# ====================================
# x = "global x"
# def what_about_lambdas_and_comprehensions():
#     # def f(y):
#     #     return (x, y)
#     # return lambda y: (x, y)
#     # same stuff in this case
#
#     l = [x * x for x in range(10)]  # comprehension: define a function and call it immediately
#     l = list(x * x for x in range(10))  # semantically equivalent
#     l = list((x * x for x in range(10)))  # define a generator then pass it into list()
#     # above 3 are the same
#
#     g = (x * x for x in range(10))  # this part is more or less equivalent to the following:
#     def gen():
#         for x in range(10):
#             yield x * x
#     g = gen()
# ====================================
# x = "global x"
# def nonlocal_and_global():
#     x = "nonlocal x"
#     def f():
#         # nonlocal x
#         # x = "overwritten nonlocal"
#         global x
#         x = "overwritten global"
#         return x
#     print(x)
#     print(f())
#     print(x)
# def main():
#     nonlocal_and_global()
#     print(x)
# main()
# ====================================
# x = "global x"
# def nonlocal_and_global():
#     better_name = "nonlocal x"
#     def f():
#         # global x
#         return x
#     print(better_name)
#     print(f())
#     print(better_name)
# def main():
#     nonlocal_and_global()
#     print(x)
# main()
# ====================================
# just a example, but don't actually do this
x = "global x"
def level_seven():
    def please_dont_do_this():
        if False:
            a = None
        def gen_func():
            nonlocal a
            for v in range(10):
                a = v
                yield v
        return gen_func(), lambda: a
    gen, fun = please_dont_do_this()

    #print(fun())
    next(gen)
    print(fun())
    next(gen)
    print(fun())
level_seven()