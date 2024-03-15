teilnehmende = ["Thomas", "Ingo", "Sara", "Lena", "Julia"]
print(teilnehmende)



# Add
teilnehmende.append("Frank")
print(teilnehmende)


teilnehmende.insert(1 , "Mattias")
print(teilnehmende)



# Edit
teilnehmende[0] = "Omid"
print(teilnehmende)


# Delete an index
teilnehmende.pop() # delete the last index --> pop(-1)
print(teilnehmende)


teilnehmende.pop(1) # delete specific index
print(teilnehmende)

teilnehmende.remove("Julia")
print(teilnehmende)



del teilnehmende[0]
print(teilnehmende)


del teilnehmende[1:3]
print(teilnehmende)



########################################
numbers = [4,8,2,5,7,1,3]
teilnehmende = ["Thomas", "Ingo","Thomas" ,"Sara", "Lena","Thomas", "Julia"]



# .count()
print(teilnehmende.count("Thomas"))


# .index()
print(teilnehmende.index("Ingo"))

# .sort()
numbers.sort()  # sorts the original container
print(numbers)


##############################################
numbers = [4,8,2,5,7,1,3]
teilnehmende = ["Thomas", "Ingo","Thomas" ,"Sara", "Lena","Thomas", "Julia"]


print(len(numbers))
print(sum(numbers))
print(max(numbers))
print(min(numbers))
print(sorted(numbers)) # sorted() creates a new sorted list without changing the original container

