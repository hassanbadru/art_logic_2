import math
import re

def encoder(input_num):
  #user input
  # input_num = input("Value to Encode: ")

  #binary to hex lookup dictionary
  b2h_lookup = {
    '0000': '0', '0001': '1',
    '0010': '2', '0011': '3',
    '0100': '4', '0101': '5',
    '0110': '6', '0111': '7',
    '1000': '8', '1001': '9',
    '1010': 'A', '1011': 'B',
    '1100': 'C', '1101': 'D',
    '1110': 'E', '1111': 'F'
    }

  #Function to check for integer
  def is_digit(n):
    try:
      int(n)
      return True
    except ValueError:
      return  False


  #Check if input_num is an integer
  if is_digit(input_num):

    #Inputted Integer (decimal)
    input_num = int(input_num)
    # print(input_num)

    #Check if within range of 16-bit: [-8192..+8191]
    if input_num >= -8192 and input_num <= 8191:

      #Intermediate Integer (decimal)
      num = input_num + 8192


      #Decimal to binary conversion
      bin_num = ''
      rem = 0

      while num > 0:
        rem = int(num % 2)  #remainder
        bin_num += str(rem) #add remainder to string
        num = math.floor(num / 2)

      #Check number of bits used by integer
      n_bits = len(bin_num)

      #Check if integer is 16-bit or less (binary)
      if n_bits < 16:
        add_bits = 16 - n_bits

        #if less, pad num with 0s to make 16-bit
        # bin_num = bin_num + '0' * add_bits

        #Intermediate (binary)
        bin_num = '0' * add_bits + bin_num[::-1]
        # bin_num = bin_num[::-1]  #Reverse remainders


        #Split into two 8-bits (hi bit ~ low bit)
        hi_bit = bin_num[:8]
        lo_bit = bin_num[8:]


        #Print unencoded binary (hi bit ~ low bit)
        # print(hi_bit, lo_bit)

        #Encoding Process: hi_bit ~ low bit (binary)
        hi_bit = hi_bit[1:8] + lo_bit[0]
        lo_bit = '0' + lo_bit[1:8]

        #Print encoded binary (hi bit ~ low bit)
        # print(hi_bit, lo_bit)

        #Print encoded 8-bit into two 4-bits (hi bit)
        # print(hi_bit[:4], hi_bit[4:])

        #Print encoded 8-bit into two 4-bits (low bit)
        # print(lo_bit[:4], lo_bit[4:])


        #Encoded binary to hex conversion
        h = b2h_lookup[hi_bit[:4]] + b2h_lookup[hi_bit[4:]] # hi bit

        l = b2h_lookup[lo_bit[:4]] + b2h_lookup[lo_bit[4:]] # low bit

        #Print encoded num (hex)
        output = h + l
        # print(output)
        return output
    else:
      output = "Integer value cannot exceed 16-bit range"
      # print(output)
      return output
  else:
    output = "Please enter a valid integer value"
    # print(output)
    return output

def decoder(input_num):

  # input_num = input("Value to Decode: ")

  # hex to binary lookup dictionary
  h2b_lookup = {
    '0':'0000', '1': '0001',
    '2': '0010', '3': '0011',
    '4': '0100', '5': '0101',
    '6': '0110', '7': '0111',
    '8': '1000', '9': '1001',
    'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101',
    'E': '1110', 'F': '1111'
    }

  #Check if valid string
  if input_num:
    bin_num = ''

    l_num = len(input_num)
    if l_num > 1:
        for i in input_num:

          # convert character to upper case
          if i.isalpha():
              i = i.upper()
          #Check if valid hex
          try:
            bin_num += h2b_lookup[i]
          except KeyError:
            output = "Please enter a valid hexadecimal value"
            # print(output)
            return output

        if l_num < 4:
          n_zeros = (4 - l_num) * 4
          bin_num = "0" * n_zeros  + bin_num
          # print(l_num, n_zeros)

        elif l_num > 4:
          output = "Hexadecimal value exceeds 16-bit"
          return output
    else:
          #Check if valid hex
          try:
            bin_num = h2b_lookup[input_num]
            bin_num = "0" * 12 + bin_num
          except KeyError:
            output = "Please enter a valid hexadecimal value"
            # print(output)
            return output

    # print(bin_num)

    hi_bit = bin_num[:8]
    lo_bit = bin_num[8:]

    # print(hi_bit, lo_bit)


    #Decoding Process: hi_bit ~ low bit (binary)
    lo_bit = hi_bit[7] + lo_bit[1:8]
    hi_bit = '0' + hi_bit[:7]


    # print(hi_bit + lo_bit)

    #Decoded Binary
    bin_num = hi_bit + lo_bit

    n = 0
    dec_integer = 0

    for nbit in bin_num[::-1]:
      dec_integer += int(nbit) * (2 ** n)
      # print(nbit, "* 2^" + str(n)+": ", (2 ** n),  dec_integer)
      n += 1

    output = dec_integer - 8192
    # print(output)
    return output

  else:
    output = "Please enter a valid hexadecimal value"
    # print(output)
    return output



# GET INSTRUCTIONS
def get_instructions(m_string):

  major_dict = {}

  #Find Clear
  clear_f0 = re.compile(r'F0')
  all_clear = clear_f0.finditer(m_string)

  for i in all_clear:
    key = i.start()
    major_dict[key] = 'CLR'


  #Find Pen Positions
  pen_80 = re.compile(r'80')
  all_pens = pen_80.finditer(m_string)

  for i in all_pens:
    key = i.start()

    major_dict[key] = 'PEN'


  #Find Color Changes
  color_a0 = re.compile(r'A0')
  all_colors = color_a0.finditer(m_string)

  for i in all_colors:
    key = i.start()
    major_dict[key] = 'CO'


  #Find All Moves
  move_c0 = re.compile(r'C0')
  all_moves = move_c0.finditer(m_string)

  for i in all_moves:
    key = i.start()
    major_dict[key] = 'MV'

  all_instructions = sorted(major_dict.items())

  return all_instructions


# TRANSLATE INSTRUCTIONS
def readInstruction(s1):

  my_instructions = get_instructions(s1)
  num_instructions = len(my_instructions)
  action_log = []

  for n in range(num_instructions):
    location = my_instructions[n][0]
    action = my_instructions[n][1]

    #Location of Next Instruction
    if n < num_instructions-1:
      next_location = my_instructions[n+1][0]



    if action == 'CLR':
      action_log.append("CLR")
      # print('CLR')

    if action == 'CO':
      param_location = location + 2
      param = s1[param_location:next_location]

      color_val = [decoder(param[i:i+4]) for i in range(0, len(param), 4)]

      action_log.append({"CO": color_val})
      # print('CO: ', color_val)

    if action == 'MV':
      param_location = location + 2
      param = s1[param_location:next_location]

      move_val = [decoder(param[i:i+4]) for i in range(0, len(param), 4)]

      x = move_val[0::2]
      y = move_val[1::2]

      # x_y = [i for i in zip(x, y)]

      # print([{"x": i, "y": j} for i, j in zip(x, y)])?

      # action_log.append({"MV": x_y})
      # action_log.append([{"x": i, "y": j} for i, j in zip(x, y)])


      for i, j in zip(x, y):
          action_log.append({"MV": [i, j]})

      # print('MV (x, y): ', x_y)

      # print(sum(x), sum(y))

    if action == 'PEN':
      param_location = location + 2
      param = s1[param_location:param_location+4]

      if decoder(param) == 0:
        pen_position = "PEN UP"
      else:
        pen_position = "PEN DOWN"

      action_log.append(pen_position)
      # print(pen_position)

  # print(action_log)
  return action_log

#check if value exceeds boundary, returns value if less or border if more
def fix_boundary(val):
  if val < -8192:
    return -8192
  elif val > 8191:
    return 8191
  else:
    return val



def write_instructions(instruction_stream):
  instruction_json = {}

  pen_down = False
  pen_up = False

  count = 0

  x = 0
  y = 0

  x_up = 0
  y_up = 0

  # iterate through all instructions
  for instruction in instruction_stream:

    # add clear out instruction
    if instruction == 'CLR':
      instruction_json[str(count)] = instruction
      count +=1


  # LOGIC FOR PEN UP/PEN DOWN
  # add pen up instruction
    if instruction == 'PEN UP':
      pen_down = False
      instruction_json[str(count)] = instruction
      count +=1

    # add pen down instruction
    elif instruction == 'PEN DOWN':
      pen_down = True
      instruction_json[str(count)] = instruction
      count +=1

    elif isinstance(instruction, dict):
      key = list(instruction.keys())[0]

      # add COLOR instruction
      if key == 'CO':
        instruction_json[str(count)] = instruction
        count +=1

      if key == 'MV':

        if pen_down:
          # new x, y position
          x += instruction[key][0]
          y += instruction[key][1]

          # Actual values for x, y after adjusting boundary rules
          x_temp = fix_boundary(x)
          y_temp = fix_boundary(y)


          # Check if within boundary to add pen down instruction
          if (x - x_temp == 0 and y - y_temp == 0) and pen_up:
            # instruction_json[str(count)] = {'MV': [fix_boundary(x-instruction[key][0]), fix_boundary(y-instruction[key][1])]}

            if instruction[key][0] != 0:
              slope = instruction[key][1] / float(instruction[key][0])
              # print(slope)
            else:
              slope = y

            # print("slope2: ", slope)
            yBorder = slope * (fix_boundary(x_up) - x) + y
            instruction_json[str(count)] = {'MV': [fix_boundary(x-instruction[key][0]), math.ceil(yBorder)]}
            count += 1
            # print("y2 when x > 8191: ", yBorder)
            # print('actual2: ', x, y, 'adj', x_temp, y_temp, slope, "\n\n")


            instruction_json[str(count)] = "PEN DOWN"
            pen_up = False
            count += 1

          # if (x - x_temp != 0 or y - y_temp != 0) and pen_up:
            # instruction_json[str(count)] = "PEN UP"
            # pen_up = True
            # print(instruction, x, y, x_temp, y_temp)
            # count += 1

          # add new MV instruction
          if not pen_up:


            # Check if x, y is outside boundary to add pen up instruction
            if (x - x_temp != 0 or y - y_temp != 0):

              if instruction[key][0] != 0:
                slope = instruction[key][1] / float(instruction[key][0])
              else:
                slope = y

              # print("slope1: ", slope)
              if x - x_temp != 0:
                yBorder = slope * (x_temp - x) + y
                instruction_json[str(count)] = {'MV': [x_temp, math.ceil(yBorder)]}
                count += 1

              elif y - y_temp != 0:
                xBorder = ((y_temp - y)/float(slope)) + x
                instruction_json[str(count)] = {'MV': [math.ceil(xBorder), y_temp]}
                count += 1

              elif x - x_temp != 0 and y - y_temp != 0:
                instruction_json[str(count)] = {'MV': [x_temp, y_temp]}
                count += 1

              instruction_json[str(count)] = "PEN UP"
              pen_up = True
              x_up = x
              y_up = y
              count += 1

            else:
              instruction[key] = [x_temp, y_temp]
              instruction_json[str(count)] = instruction
              count +=1

          # print(x, y)

        else:

          #x, y values when PEN UP
          x_up += instruction[key][0]
          y_up += instruction[key][1]

          # if x,y - pen up is within boundary
          if (x_up < 8191 and x_up > -8192) and (y_up < 8191 and y_up > -8192):

            x = x_up
            y = y_up

          # if x - pen up is within boundary
          elif x_up > 8191 and x_up < -8192:
              pass
              # print("x_up inside", x_up, y_up)


          # if y - pen up is within boundary
          elif y_up > 8191 and y_up < -8192:
              pass
              # print("y_up inside", x_up, y_up)

          # if x, y - pen up all outside boundary
          else:
              pass
              # print("none inside")

          # add new MV instruction
          instruction[key] = [x, y]
          instruction_json[str(count)] = instruction
          count +=1

          # print(x, y, x_up, y_up)



  return instruction_json

# # s2 = 'F0A04000417F4000417FC040004000804001C05F205F20804000'
#
# s2 = 'F0A040004000417F417FC04000400090400047684F5057384000804001C05F204000400001400140400040007E405B2C4000804000'
#
# # s2 = 'F0A0417F40004000417FC067086708804001C0670840004000187818784000804000'
#
# # s2 = 'F0A0417F41004000417FC067086708804001C067082C3C18782C3C804000'
#
# readInstruction(s2)
