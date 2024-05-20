def minimum_rotations(name):
    total_rotations = 0
    current_position = 'a'

    for char in name:
        current_index = ord(current_position) - ord('a')
        target_index = ord(char) - ord('a')
        
        clockwise_distance = (target_index - current_index) % 26
        counterclockwise_distance = (current_index - target_index) % 26
        
        total_rotations += min(clockwise_distance, counterclockwise_distance)
        current_position = char
    
    return total_rotations

name = input().strip()

print(minimum_rotations(name))
