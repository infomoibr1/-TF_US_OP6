# Lambda :: Anonym Function (without name) , gibt mir eine Memory Adresse zurück


# 1. Classical Function
def add(x, y):
    return x + y 

# 2. Lambda Function

apfel = lambda x,y : x + y

result = apfel(3,5)
print(result)



# Self Study 
# - Lambda with filter(), map() , [].sort()