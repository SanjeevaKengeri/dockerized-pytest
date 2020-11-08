class Point():
    def __init__(self,name,latitude,longitude):
        self._name = name
        self._latitude = latitude
        self._longitude = longitude
    #if we want to make sure that these instance objects 
    #are not accessible to the average user we should 
    #put a _ in front of each one.
    
    def get_lat_long(self):
        return (self._latitude,self._longitude)
