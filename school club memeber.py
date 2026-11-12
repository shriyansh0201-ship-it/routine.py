name = input("Enter your Member name")
club = input("Enter your club name")
memeber_number = 8
points = 9.5
is_active = True
print("Member Number:", memeber_number, "=type:", type(memeber_number))
print("Points:", points, "= type:", type(points))
print("Active:", is_active, "= type:", type("is_active"))
badge_code = name[0:3] + club[-1] + str(memeber_number)
print("badge_code:", badge_code)
print("==== Club badge ====")
print("Member:" + name)
print("Club:"   +  club)
print("Code:"   +  badge_code)
print("Points:  " +   str(points) +  "  | " + "Active: " + str(is_active))