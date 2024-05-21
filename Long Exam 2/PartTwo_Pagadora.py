# OOP Prblem 1 first step creating class Parcel
class Parcel:
    '''
    Description of the parcel provided name of the owner and the area of lot
    '''
    def __init__(self, owner, area):
        self.owner = owner
        self.area = area

    def getClassification(self):
        '''
        getting the land classification based on area
        '''
        area = area
        if area < 10000:
            Classification = "Residential"
            return str(Classification)
        elif area > 10000 and area < 120000:
            Classification= "Private Agricultural"
            return str(Classification)
        elif area > 120000:
            Classification = "Public Agricultural"
            return str(Classification)
        else:
            Classification = "Unknown"
            return str(Classification)
        
def PrintOverload(owner, area):
    '''
    print overload
    not so sure po about this part
    '''
    print("A parcel of land owned by " + str(owner) + " with an area of " + str(area) + " square meters")

def printAdd(self_owner, self_area, other_area, other_owner):
    '''
    print
    not so sure po about this part
    '''
    sumArea = self_area + other_area
    print("Consolidate lot of" + str(self_owner) + " and " + str(other_owner) + "with a total area of " + str(sumArea))


class Riparian(Parcel):
    def __init__(self, owner, area, Type):
        self.Type = Type
        super().__init__(owner, area)
        
    
    def getAdjoiningWaterbody(self):
        Type = Type
        if Type == 1:
            type = "Adjacent to River - can be subject to titling"
            return str(type)
        elif Type == 2:
            type = "Adjacent to Ocean (Littoral) - cannot be subject to titling"
            return str(type)
        else:
            type = "Invalid Riparian Parcel"
            return str(type)
        

