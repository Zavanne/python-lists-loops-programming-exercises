parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

# Your code here
def get_parking_lot(parking_state):
  parking_state_dict = {"total_slots": 0, "available_slots": 0, "occupied_slots": 0}
  for arr in parking_state:
      
      for element in arr:
          if element == 1:
              parking_state_dict["occupied_slots"] += 1
              parking_state_dict["total_slots"] += 1
          elif element == 2:
              parking_state_dict["available_slots"] += 1
              parking_state_dict["total_slots"] += 1
          
  return parking_state_dict

print(get_parking_lot(parking_state))

    # Iterate over each row and column in the parking_state matrix
    # for row in parking_state:
    #     for spot in row:
    #         if spot == 1:
    #             parking_state_dict["occupied_slots"] += 1
    #         elif spot == 2:
    #             parking_state_dict["available_spots"] += 1
    #         # Total slots count can be incremented based on non-zero values
    #         if spot in (1, 2):
    #             parking_state_dict["total_slots"] += 1