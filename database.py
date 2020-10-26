from model import Artist, Artwork
from peewee import IntegrityError
from model import db


def add_artist(name, email):#adding new artist
    try:
        Artist(name = name, email = email).save()
        # print("you added new name")
    except IntegrityError as e:
        # you could log the error e here if needed
        return 'Duplicate artist name'
    
def find_artist(name):# geting an artist by artist name
    artist =Artist.get(Artist.name == name)
    if artist:
        return artist.id
         
def add_artwork(artist, name, price):#adding new artwork
    try:
        artist_id = find_artist(artist)
        if artist_id:
            Artwork.create(artist = artist_id ,name = name, price = price).save
            print('art work added succesfully')
        else:
            print("not found")
    except IntegrityError as e:
       return 'error adding artwork because' + str(e)
    # except:
    #     print("art work not add")

def get_all_artwork_of_artist(name):#returning all artwork by artist

   
    try:
        artwork_list = []
        artist_id = find_artist(name)
        for art in Artwork.select().where(Artwork.artist == artist_id):
            artwork_list.append(art.name)

        # what about the price, and is it available? Better to return a list of Artwork objects 
        return ', '.join(artwork_list)
    except:
        print('no found an art')  # if there's nothing found, you won't get an excption 

def get_available_artwork_of_artist(name):#returnig all available artwork by artist

    

    artwork_list = []

    for art in Artwork.select().join(Artist).where(

        (Artist.name == artist) & (Artwork.available == True)):

        artwork_list.append(art.Artwork.name)

    return ', '.join(artwork_list)

def change_availibility_status_to_available_or_sold( available, art_id):# gets artwork by ID and updates it's availibility status.

    

    art = Artwork.update(is_available = available).where(Artwork.id == art_id)

    updated_row = art.execute()

    return updated_row



def delete_artwork(name):# deleting by artwork name
    delete_row = Artwork.delete().where(Artwork.name == name).execute()
    if not delete_row:
        print("art not deleted")
    else:
        print('you deleted succesfully')
        #raise ArtError('tried to delete that does not exist')




