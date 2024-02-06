total_pool = 2 #\beta
total_balls_o = 4 #\theta
total_balls = total_balls_o
red_balls = 1 #target
white_balls = total_balls - red_balls
expected_att = 0
expected_prob = 0

att_flag = 0
att = 1
round = 1

while red_balls < total_balls:
    print(att)
    probability = 1

    i = 1
    att_flag_i = 0
    while i < round:
        probability *= (white_balls - i + 1) / (total_balls_o - i + 1)
        att_flag_i += 1
        if att_flag_i == total_pool:
            att_flag_i = 0
            i += 1

    probability *= red_balls / (total_balls)

    expected_att += att * probability

    att += 1
    att_flag += 1
    if att_flag == total_pool:
        att_flag = 0
        total_balls -= 1
        round += 1

print(expected_att)
