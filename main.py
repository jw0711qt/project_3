import ui

from model import Artist, Artwork
import database
def main():
    while True:
        choice = ui.menu_choice()
        if choice == '1':
            add_artist()
        elif choice == '2':
            add_artwork()
        elif choice == '3':
            get_available_artwork_of_artist(name)

        elif choice == '4':
            get_all_artwork_of_artist()
        elif choice == '5':
            change_availability()
        elif choice == '6':
            delete_art_work()
        
        elif choice == 'q':
            break

def add_artist():# adding artist
    name=ui.get_string('Enter name of  the Artist')
    
    email = ui.get_string(f'Enter email for {name}')
    database.add_artist(name,email)

def add_artwork():# adding art work
    name= ui.get_string('Enter name of the art work')
    
    price = ui.get_postive_float('Enter art price ')
    artist = ui.get_string('Enter name of artist')
    
    database.add_artwork(artist, name, price) 

def get_all_artwork_of_artist():# searching for all art work by artist
    name= ui.get_string ('Enter name ')

    try:
        database.get_all_artwork_of_artist(name)
    except:
        print ('no found ant art')
    

def get_available_artwork_of_artist(name):#searching for available artwork
    name = ui.get_string('enter the of artist the one you want to see his/her arts')
    
    database.get_available_artwork_of_artist(name)
   

def change_availability():#change the availabilty by id
    id =  get_artwork_id()
    availability = ui.get_is_available_value()
    
    database.change_availibility_status_to_available_or_sold()(id, availability)
    

def delete_art_work():#deleting by artwork name
    name = ui.get_string("enter art work name")

    database.delete_artwork(name)
    


if __name__ == '__main__':
    main()


                        
            
            