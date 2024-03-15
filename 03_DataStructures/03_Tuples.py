
# Tuples are READ ONLY containers
###################################

teilnehmende = ("Thomas", "Ingo","Thomas" ,"Sara", "Lena","Thomas", "Julia")
print(teilnehmende, type(teilnehmende))


for tn in teilnehmende:
    print(tn)


####################################################
# Work arround
    
teilnehmende = ("Thomas", "Ingo","Thomas" ,"Sara", "Lena","Thomas", "Julia")
print(teilnehmende)



tmp_list = list(teilnehmende)
tmp_list.append("Michael")

teilnehmende = tuple(tmp_list)  # neu angelegt (dynamic)

print(teilnehmende)


###################################################
# Mutable in Tuples --> Special case

my_tuple = ("Thomas", "Ingo", [], "Sara")
print(my_tuple)


my_tuple[2].append("AAAA")
print(my_tuple)