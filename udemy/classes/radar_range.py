# Radar Range

car_speed = 61
car_local = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

taxed_car = (LOCAL_1 - RADAR_1) <= car_local <= (LOCAL_1 + RADAR_RANGE)

if car_speed > RADAR_1:
    print('The car speed pass of radar')

if taxed_car and car_speed > RADAR_1:
    print('The car was taxed')
