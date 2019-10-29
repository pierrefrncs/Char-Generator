import random
# declaration of our dictionary, used as a HashMap
Map = {}
Map['A']=0.08167
Map['B']=0.01492
Map['C']=0.02782
Map['D']=0.04253
Map['E']=0.12702
Map['F']=0.02228
Map['G']=0.02015
Map['H']=0.06094
Map['I']=0.06966
Map['J']=0.00153
Map['K']=0.00772
Map['L']=0.04025
Map['M']=0.02406
Map['N']=0.06749
Map['O']=0.07507
Map['P']=0.01969
Map['Q']=0.00095
Map['R']=0.05987
Map['S']=0.06327
Map['T']=0.09056
Map['U']=0.02758
Map['V']=0.00978
Map['W']=0.02360
Map['X']=0.00150
Map['Y']=0.01974
Map['Z']=0.00074

distSum =1
key: str

# if needed this function allows you to add values to the dictionary

# def addCharacter(a, b):
#    global distSum
#    if Map.get(a)!= None:
#        distSum -= Map.get(a)
#    Map[a]=b
#    distSum+=b


# gives you a random character based on it's statistical appearance

def getcharacter():


    tempdist = 0
    temp = random.random()
    ratio = 1/distSum
    for i in Map.keys():
        tempdist += Map.get(i)
        if (temp/ratio) <= tempdist:
            return i
    return 0
