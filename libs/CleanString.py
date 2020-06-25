class CleanString:
    str =""
    def __init__(self,str1):
        self.str = str1
        print(self.str)
    def clear (self):
        lista = ["<",">","=","+","-","'",'"',","]
        # st = self.str
        str2 =""
        print(self.str)
        cont = 0
        for x in  self.str:
            b =  x in lista
            # print(b)
            if b == False:
                str2 += self.str[cont]
            cont +=1
        print(str2)
        
        return str2
    

    
        