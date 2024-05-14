import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)

hour = int(time.strftime("%H"))

if hour > 6 and hour < 12: 
    print("Good Morning")
elif hour > 12 and hour < 18: 
    print("Good Everning")
else: 
    print("Good Night")