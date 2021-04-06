def d_movement_speed(undiminished_movement_speed):
    # undiminshed_movement_speed = sum(movement_speed_list)
    if(undiminished_movement_speed <= 457):
        return undiminished_movement_speed
    if(undiminished_movement_speed > 457 and undiminished_movement_speed <= 540.5):
        return 457 + ((undiminished_movement_speed - 457) * 0.8)
    if(undiminished_movement_speed > 540.5 and undiminished_movement_speed <= 1000):
        return 523.8 + ((undiminished_movement_speed - 540.5) * 0.5)
    return 753.55

def undim_ms (base, percent_ms):
    return base + ((base*percent_ms)/100)

def ms_calculator (base, item_list):
    percent_ms = 0
    for item in item_list:
        percent_ms += item.ms or 0
    return d_movement_speed(undim_ms(base, percent_ms))