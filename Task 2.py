time = int(input("Введите время в секундах: "))
hour = time // 3600
min = (time % 3600) // 60
sec = time - hour * 3600 - min * 60
if hour < 10:
    hour = str("0"+str(hour))
else:
    hour = str(hour)

if min < 10:
    min = str("0" + str(min))
else:
    min = str(min)

if sec < 10:
    sec = str("0"+str(sec))
else:
    sec = str(sec)

print(hour+":"+min+":"+sec)