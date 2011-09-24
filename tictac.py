

prev_array_num_user_row=0
prev_array_num_user_col=0
prev_array_num_comp_row=0
prev_array_num_comp_col=0
array = [
         [0,0,0],
         [0,0,0],
         [0,0,0]
        ]

# Returns 
# the col number when there is a success
# else
# -1 if there is no success

def check_row_for_two_identical_elements_and_an_empty_space(row, tobecheckedelement):
  count = 0
  for i in range(0,3):
    if ((array[row][i] == tobecheckedelement) or
         (array[row][i] == 0)):
      count += 1
      if (array[row][i] == 0):
        emptySpace = i

  if count == 3:
     return emptySpace
  else:
     return -1
 
# Returns 
# the row number when there is a success
# else
# -1 if there is no success

def check_col_for_two_identical_elements_and_an_empty_space(col, tobecheckedelement):
  count = 0
  for i in range(0,3):
    if ((array[i][col] == tobecheckedelement) or
         (array[i][col] == 0)):
      count += 1
      if (array[i][col] == 0):
        emptySpace = i

  if count == 3:
     return emptySpace
  else:
     return -1

# Returns 
# the row/col number when there is a success (since row == col; only one val is enough as return val)
# else
# -1 if there is no success

def check_lowtohigh_for_two_identical_elements_and_an_empty_space(tobecheckedelement):
  count = 0
  for i in range(2, -1, -1):
    if ((array[i][2-i] == tobecheckedelement) or
         (array[i][2-i] == 0)):
      count += 1
      if (array[i][2-i] == 0):
        emptySpace = i

  if count == 3:
     return emptySpace
  else:
     return -1

# Returns 
# the row/col number when there is a success (since row == col; only one val is enough as return val)
# else
# -1 if there is no success

def check_hightolow_for_two_identical_elements_and_an_empty_space(tobecheckedelement):
  count = 0
  for i in range(0, 3):
    if ((array[i][i] == tobecheckedelement) or
         (array[i][i] == 0)):
      count += 1
      if (array[i][i] == 0):
        emptySpace = i

  if count == 3:
     return emptySpace
  else:
     return -1

# if (there are three consecutive matches by 'comp')
#   return 1
# else
#   return 0

def check_last_add_by_comp():
  global prev_array_num_comp_row
  global prev_array_num_comp_col
  
  if (check_row_for_two_identical_elements_and_an_empty_space(prev_array_num_comp_row,2) != -1 or
       check_col_for_two_identical_elements_and_an_empty_space(prev_array_num_comp_col,2) != -1 
     ):
     return 1
  elif (((prev_array_num_comp_row + prev_array_num_comp_col) != 1) or ((prev_array_num_comp_col + prev_array_num_comp_row)!= 3)):
     if ((prev_array_num_comp_row == 1) or (prev_array_num_comp_col == 1)):     
        if (check_lowtohigh_for_two_identical_elements_and_an_empty_space(2) != -1 or       
             check_hightolow_for_two_identical_elements_and_an_empty_space(2) != -1):
              return 1

     if (prev_array_num_comp_row == 0):
       if(check_hightolow_for_two_identical_elements_and_an_empty_space(2) != -1):
         return 1
     else:
       if(check_lowtohigh_for_two_identical_elements_and_an_empty_space(2) != -1):
         return 1

  else:
     return 0   

# if (there are three consecutive matches by 'comp')
#   return 1
# else
#   return 0

def check_last_add_by_user():
  global prev_array_num_user_row
  global prev_array_num_user_col

  ret_row = check_row_for_two_identical_elements_and_an_empty_space(prev_array_num_user_row,1)
  ret_col = check_col_for_two_identical_elements_and_an_empty_space(prev_array_num_user_col,1)
  if ( ret_row != -1 ):
     prev_array_num_user_col = ret_row 
     return 1
  elif (ret_col != -1):
     prev_array_num_user_row = ret_col
     return 1

  elif (((prev_array_num_user_row + prev_array_num_user_col) != 1) or ((prev_array_num_user_col + prev_array_num_user_row)!= 3)):
     ret_lowhigh = check_lowtohigh_for_two_identical_elements_and_an_empty_space(1)
     ret_highlow = check_hightolow_for_two_identical_elements_and_an_empty_space(1)

     if ((prev_array_num_user_row == 1) or (prev_array_num_user_col == 1)):     
        if ( != -1 or       
             check_hightolow_for_two_identical_elements_and_an_empty_space(1) != -1):
              return 1

     if (prev_array_num_comp_row == 0):
       if(check_hightolow_for_two_identical_elements_and_an_empty_space(2) != -1):
         return 1
     else:
       if(check_lowtohigh_for_two_identical_elements_and_an_empty_space(2) != -1):
         return 1

  else:
     return 0   
def check_last_add_by_user():
  return 1

def complete_tic_tac_game():
  global prev_array_num_user_row
  global prev_array_num_user_col
  global prev_array_num_comp_row
  global prev_array_num_comp_col
  global array

  while (True):

   if (check_last_add_by_comp()):
    print "Game won by the computer :) :) :)"
    return  

   if (check_last_add_by_user()):
    array[prev_array_num_comp_row][prev_array_num_comp_col]=2
   else:
    print "This game is a draw"
    return 

   row = raw_input("Enter the row :- ")
   col = raw_input("Enter the col :- ")
 
   prev_array_num_user = row * 3 + col
   array[prev_array_num_user]=1

if __name__ == "__main__":
  global prev_array_num_user_row
  global prev_array_num_user_col
  global prev_array_num_comp_row
  global prev_array_num_comp_col
  global array

  print "r1c1 | r1c2 | r1c3\n"
  print "------------------\n"
  print "r2c1 | r2c2 | r2c3\n"
  print "------------------\n"
  print "r3c1 | r3c2 | r3c3\n"


  row = int(raw_input("Enter the row :- "))
  col = int(raw_input("Enter the col :- "))
  # Set the user selected element to 1
  array[row][col] = 1

  prev_array_num_user_row = row
  prev_array_num_user_col = col

  # Set the comp selected element to 2
  array[1][1] = 2

  prev_array_num_comp_row = 1
  prev_array_num_comp_col = 1

  complete_tic_tac_game() 
