from pkg.sub1.mod1 import func1_mod1


def func1_mod3():
    print('func1_mod3 -> NOW CALLS -> func1_mod1')
    func1_mod1()
