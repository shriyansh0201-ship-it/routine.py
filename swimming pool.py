print("Answer 3 questions and i will tell you which pool you can swim in.\n")
age = int(input("How old are you "))
can_swim = input("Can you swim 25 meters? (yes/no): ").lower()
adult_here = input("Is an adult with you? (yes/no):").lower()
print("-" * 32)
if age < 4:
    print("Age group : Toddler -splash pool only,always with an adult.")
elif age < 12:
    print("Age group : Child - main pool with an adult.")
elif age < 18:
    print("Age group : Teen - Main pool alone if you can swim.")
else:
    print("Age group : Adult - All pools are open to you.")
if can_swim != "yes" and can_swim != "no":
    print("Input error : Please answer the adult question with yes or no.")
    adult_known = "false"
else:
    adult_known = "True"
    if can_swim =="yes"and adult_here =="yes":
     print("Deep pool  : Allowed - you can swim and an adult is present")
if age < 12 or can_swim =="no":
   print("Shallow only: Stay in the shallow end today")
if adult_known - True and not(adult_here == "yes"):
     print("Reminder    :no adult with you - the lifeguard must be told.")
if can_swim == False or adult_here == False:
    print("Verdict    :Cannot decide until both questions are answerd properly")
elif age >= 18 and can_swim == "yes":
    print("Verdict   : Full access,enjoy your swim.")
elif age >= 12 and can_swim == "yes":
    print("Main pool access with adult nearby")
elif can_swim == "no" and not (adult_here =="yes"):
 print("Verdict    :Shallow end only, please find an adult first")
else:
 print("Verdict     :Shallow end today - come back with an adult for more.")
print()
print("Have a safe swim")