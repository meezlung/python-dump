time = input().split(':')
minutes = int(input())
new_time = []

for t in time:
    new_time.append(int(t))

new_time[1] += minutes
if new_time[1] >= 60:
    howManyMins = new_time[1] // 60
    time[1] -= 60*howManyMins
    time[0] += howManyMins
if new_time[0] >= 24:
    howManyHours = new_time[0] // 24
    time[0] = time[0] - 24*howManyHours

newTime = [str(t).zfill(2) for t in time]
joinTime = str(":".join(newTime))
print(joinTime) 
