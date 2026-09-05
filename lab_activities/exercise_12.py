# ============================================================
# CMPE 201 Section2-2 - Data Structures and Algorithm
# Exercise 12: Mutable Lists and id()
# Submitted by GROUP 5
# Ferrer, Angelo Terrence D.
# Flores, Prince Menard T.
# Guillen, Rod John F.
# Mayor, John Luis V.
# Pagdanganan, Kryzle Camille S.
# ============================================================

#Run the starter program
li = [1, 2, 3]
print("Initial list:        ", li)
print("Initial memory id:   ", id(li))

#Modifying the first element in place
li[0] = 10
print("\nAfter li[0] = 10:    ", li)
print("Memory id after edit:", id(li))

#Repeat using li.append(20) and inspect id(li)
li.append(20)
print("\nAfter append(20):    ", li)
print("Memory id after add: ", id(li))