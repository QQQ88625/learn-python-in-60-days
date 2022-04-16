# strict rule should be execute at first, otherwise it would lead to mistake
gender = "male"
body = "fat"

if gender == "male" and body == "fat":
    print("loser 1")
elif body == "fat":
    print("loser 2")


if body == "fat":
    print("loser 2")
elif gender == "male" and body == "fat":
    print("loser 1")