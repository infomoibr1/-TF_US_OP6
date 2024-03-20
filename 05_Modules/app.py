
import greetings 

greetings.greeting_de("Mohamed")
greetings.greeting_en("Mohamed")
print(greetings.location)
 
##################################################
# Alias (Nickname)

import greetings as gt 

gt.greeting_fr("Mohamed")
print(gt.location)

###################################################
# import specific elements
from greetings import greeting_sp, greeting_tr, location


greeting_tr("Ertugrul")
greeting_sp("Ertugrul")

print(location)

###################################################
# import specific elements with Alias
from greetings import greeting_sp as sp , greeting_tr as tr 


sp("Susanne")
tr("Susanne")



######################################################
# import all elements as local functions
from greetings import * 

greeting_cn("Lena")
greeting_tr("Michele")

print(company)
 




 