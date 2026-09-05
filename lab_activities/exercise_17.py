# ============================================================
# CMPE 201 Section2-2 - Data Structures and Algorithm
# Exercise 17: Student Scores Processor
# Submitted by GROUP 5
# Ferrer, Angelo Terrence D.
# Flores, Prince Menard T.
# Guillen, Rod John F.
# Mayor, John Luis V.
# Pagdanganan, Kryzle Camille S.
# ============================================================


# Starter data
scores = [72, 55, 89, 64, 91, 48, 77, 60]
# Keep a reference copy to verify Step 53
original_reference = scores.copy()

#Create passed using a filtered list comprehension (threshold >= 60)
passed = [s for s in scores if s >= 60]

#Create squares using a regular list comprehension
squares = [s ** 2 for s in scores]

#Display all three lists and verify the original list is unchanged
print("Original scores:", scores)
print("Passing scores: ", passed)
print("Squared scores: ", squares)
print("Is scores unchanged?:", scores == original_reference)