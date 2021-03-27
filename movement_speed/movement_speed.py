def d_movement_speed(undiminshed_movement_speed):
    if(undiminshed_movement_speed <= 457):
        return undiminshed_movement_speed
    if(undiminshed_movement_speed > 457 and undiminshed_movement_speed <= 540.5):
        return 457 + ((undiminshed_movement_speed - 457) * 0.8)
    if(undiminshed_movement_speed > 540.5 and undiminshed_movement_speed <= 1000):
        return 523.8 + ((undiminshed_movement_speed - 540.5) * 0.5)
    return 753.55