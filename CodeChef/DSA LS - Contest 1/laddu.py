T = int(input())
activs = {"CONTEST_WON": 300, "TOP_CONTRIBUTOR": 300, "BUG_FOUND": "True", "CONTEST_HOSTED": 50}
for _ in range(T):
    activities, origin = input().split()
    activities = int(activities)
    laddus = 0
    for i in range(activities):
        activity = input()
        try:
            bitch, value = activity.split(" ")
        except ValueError:
            bitch = activity
        if bitch in activs:
            try:
                if bitch == "CONTEST_WON" and int(value) < 20:
                    laddus += activs[bitch] + (20 - int(value))
                else:
                    laddus += activs[bitch]
            except TypeError:
                laddus += int(value)
    if origin == "INDIAN":
        print(laddus//200)
    else:
        print(laddus//400)



