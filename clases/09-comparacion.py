class Coordenadas:
    
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
     
    def __eq__(self, otro): # este es otro método mágico significa igual
        return self.lat == otro.lat and self.lon == otro.lon
     
    # def __ne__(self, otro): # este significa no es igual
    #     return self.lat != otro.lat or self.lon != otro.lon 
      
    def __lt__(self, otro): # este significa menor que
        return self.lat + self.lon < otro.lat + otro.lon
 
    def __le__(self, otro): # este significa menor o igual
        return self.lon + self.lat <= otro.lon + otro.lat        
            
cords1 = Coordenadas(44,27)
cords2 = Coordenadas(45,27)
# print(cords1 != cords2)        
print(cords1 <= cords2)