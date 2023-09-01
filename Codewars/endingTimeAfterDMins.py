time = input().split(':')
minutes = int(input())

for x in range(0, len(time)):
    time[x] = int(time[x])
print(time)

time[1] += minutes
if time[1] >= 60:
    howManyMins = time[1] // 60
    time[1] -= 60*howManyMins
    time[0] += howManyMins
if time[0] >= 24:
    howManyHours = time[0] // 24
    time[0] = time[0] - 24*howManyHours

newTime = [str(t).zfill(2) for t in time]
joinTime = str(":".join(newTime))
print(joinTime) 
