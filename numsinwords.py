'''
Create a dictionary to hold values representing  numbers with;
one, two, three and four digits.

Accept user input
'''

units = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}

tens = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'Seventy',
    8: 'eighty',
    9: 'ninety',
}

hundreds = {
    1: 'One hundred',
    2: 'Two hundred',
    3: 'Three hundred',
    4: 'Four hundred',
    5: 'Five hundred',
    6: 'Six hundred',
    7: 'Seven hundred',
    8: 'Eight hundred',
    9: 'Nine hundred'
}

thousands = {
    1: 'One thousand',
    2: 'Two thousand',
    3: 'Three thousand',
    4: 'Four thousand',
    5: 'Five thousand',
    6: 'Six thousand',
    7: 'Seven thousand',
    8: 'Eight thousand',
    9: 'Nine thousand'
}

def nums_in_words():
    num = input('enter ur no: ')
    output = ''
    # Validate input to ensure only digits are entered by the user to prevent program crash.
    try:
        int(num) == True
    except:
        return 'Invalid entry'    

    if(int(num) == 0):
        return 'Zero'

    # Validate entry does not exceed four digits
    elif len(num) > 4:
        return 'Input is out of range'   


    # '''
    # Search specified dictionary for values using indices of the input characters. 
    # Concatinate result with "output variable".
    # Ensure for every dictionary search, if no value is found concatinate "output variable" with an empty string
    # '''

    
    elif len(num) == 4:
        output += thousands.get(int(num[0])) + ' '
        output += hundreds.get(int(num[1]), '') + ' '
        output += tens.get(int(num[2]), '') + ' and '
        output += units.get(int(num[3]), '')


    elif len(num) == 3:
        output += hundreds.get(int(num[0])) + ' '
        output += tens.get(int(num[1]), '') + ' and '
        output += units.get(int(num[2]), '')
        

    elif len(num) == 2:
        output += tens.get(int(num[0]), '')
        output += units.get(int(num[1]), '')


    else:
        output += units.get(int(num))

    return output   


print(nums_in_words());        

