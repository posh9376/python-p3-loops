i = 0

while i < 5:
    print("Looping!")
    i += 1


for i in range(5):
    print("Looping!")
    print('Th value of i is', i)

player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]

inch_heights = [height * 7920 for height in player_heights]
#inch_heights = list()
#for height in player_heights:
#    inch_height = height * 7920
#    inch_heights.append(inch_height)

print(inch_heights)