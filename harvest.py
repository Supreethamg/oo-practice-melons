############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""
    name = ""
    reporting_code = ""
    first_harvest = ""
    color = ""
    
    is_seedless = False
    is_bestseller = False


    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.name=name
        self.reporting_code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless= is_seedless
        self.is_bestseller = is_bestseller

        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings = pairing

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.reporting_code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Creating objects of MelotType class.
    muskmelon = MelonType ('musk','1998','green',True,True,'Muskmelon')
    casaba = MelonType ('cas','2003','orange',True,False,'Casaba')
    crenshaw = MelonType ('cren','1996','green',True,False,'Crenshaw')
    watermelon = MelonType ('yw','2013','yellow',True,True,'Watermelon')

    #add necessary pairings to the instance’s pairings attribute.
    muskmelon.add_pairing(['mint'])
    casaba.add_pairing(['mint','strawberry'])
    crenshaw.add_pairing(['proscuitto'])
    watermelon.add_pairing(['ice cream'])

    #Assign all melons to the melons list
    all_melon_types = [muskmelon,casaba,crenshaw,watermelon]
    
    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f'\n{melon.name} pairs with')
        for pair in melon.pairings:
            print(f'  - {pair} ')

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # create a dictionary
    melon_by_code ={}

    #Add reporting code of a melon as key and melon object as value
    for melon in melon_types:
        melon_by_code[melon.reporting_code] = melon
    return melon_by_code


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    melon_type = ''
    shape_rating = None
    color_rating = None
    field_no = None
    harvested_by = ''

    def __init__(self,melon_type,shape_rating,color_rating,field_no,harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field_no = field_no
        self.harvested_by = harvested_by

    def is_sellable(melon):
        '''checks if melon is sellable. Return true if shape and color rating >5 and 
        melon field no is not 3 .'''
        return (melon.shape_rating > 5 and melon.color_rating > 5) and (melon.field_no != 3)



    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melons =[]
    #get look up dictionary
    melon_lookup = make_melon_type_lookup(melon_types)
    #create melon objects
    melon_1= Melon(melon_lookup["yw"],8,7,2,'Sheila')
    melon_2= Melon(melon_lookup["yw"],3,4,2,'Sheila')
    melon_3= Melon(melon_lookup["yw"],9,8,3,'Sheila')
    melon_4= Melon(melon_lookup["cas"],10,6,35,'Sheila')
    melon_5= Melon(melon_lookup["cren"],8,9,35,'Michael')
    melon_6= Melon(melon_lookup["cren"],8,2,35,'Michael')
    melon_7= Melon(melon_lookup["cren"],2,3,4,'Michael')
    melon_8= Melon(melon_lookup["musk"],6,7,4,'Michael')
    melon_9= Melon(melon_lookup["yw"],7,10,3,'Sheila')
    #Add melon objects to the list.
    melons=[melon_1,melon_2,melon_3,melon_4,melon_5,melon_6,melon_7,melon_8,melon_9]
    return melons
    

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable():
            message='(CAN BE SOLD)'
        else:
             message='(NOT SELLABLE)'

        #Print the melon details and it is sellable or not.
        print(f'Harvested by {melon.harvested_by} from Field {melon.field_no} {message}')


melon_types_list= make_melon_types()
lookup = make_melon_type_lookup(melon_types_list)
#print_pairing_info(melon_types_list)
melons_list = make_melons(melon_types_list)
get_sellability_report(melons_list)