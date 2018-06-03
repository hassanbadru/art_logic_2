import math

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
