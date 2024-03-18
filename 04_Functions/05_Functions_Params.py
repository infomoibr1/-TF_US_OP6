# The order of the parameters of greeting should be followed

def greeting(first_name, last_name, location = "berlin", *xarg, **kwarg):
    print(first_name, last_name, location, xarg, kwarg)





greeting("Thomas", "Meier", "Aachen", 1,2,3,4,5, car = "VW", kids = 2)