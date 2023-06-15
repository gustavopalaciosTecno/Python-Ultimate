class Lista(list):
    
    def prepend(self, items):
        self.insert(0,items)
        
        
lista = Lista([1,2,3,4,5,6,7])
lista.append(8) 
lista.prepend(0)
print(lista)       
           
