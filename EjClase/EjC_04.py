def celsius_a_fahrenheit(temp):
    for temp in temp:
        dic = {}
        Faren = (temp*1.8)+ 32
        dic[temp] = Faren
        print(dic)
    
        
        
        
temp = [0, 10, 20, 30, 40, 100]
celsius_a_fahrenheit(temp)