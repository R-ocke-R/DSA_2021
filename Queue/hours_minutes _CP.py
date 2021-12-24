def hours_minutes(H,M):
    ha=((360//12)*H)+(30/60)*M
    ma=(360//60)*M
    ma2=360-ma
    return int(min(abs(ha-ma), abs(ha-ma2)))

print(hours_minutes(1,59))
print(hours_minutes(6, 30))
