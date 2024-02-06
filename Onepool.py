total_balls_o = 8
total_balls = total_balls_o
red_balls = 2
white_balls = total_balls - red_balls
expected_rounds = 0


for round in range(1, total_balls - red_balls + 2):

    probability = 1
    i = 1
    while i < round:
        probability *= (white_balls - i + 1) / (total_balls_o - i + 1)
        i += 1

    probability *= red_balls / (total_balls)

    expected_rounds += round * probability

    total_balls -= 1

print(expected_rounds)
