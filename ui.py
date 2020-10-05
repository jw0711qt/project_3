from model import Artist, Artwork

def menu_choice():# creating menu
    
        response = get_string('Enter choice')
        if response in ['1','2','3','4','5','6','7','q']:
            return response
        print('invalid choice. please enter  numbers from 1-7,and q to quit')




def get_string(question, max_length=None):#checking empty string
    while True:
        response = input(f'{question}:')
        if response:
            return response
        print("please enter something. Empty not allowe")

def get_postive_float(question):# allowing only positive number to input
    while True:
        try:
            response = float(input(f'{question}:'))
            if response >= 0:
                return response
            else:
                print("please enter postive number")
        except ValueError:
            print('please enter a number')

def get_is_available_value():
    """ Ask user to enter 'available' or 'sold'
     :returns: True if user enters 'available' or False if user enters 'sold' """
    while True:
        response = input('Enter \'available\' if art work is available or \'sold\' if art work is sold: ')
        if response.lower() in ['available', 'sold']:
            return response.lower() == 'available'
        else:
            print('Type \'available\' or \'sold\'')

def get_artwork_id():
    while True:
        try:
            response = int(input('enter art id'))
            if response >= 0:
                return response
            else:
                print("please enter postive number")
        except ValueError:
            print('please enter a number')





            
