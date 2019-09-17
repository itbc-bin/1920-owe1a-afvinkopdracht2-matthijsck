seq = input("aantal nucleotiden van een sequentie") #vraagt degene die dit gebruikt hoeveel nucleotiden van een sequentie
A = seq.count("A") #aantal A in een sequntie
T = seq.count("T") #aantal T in een sequentie
G = seq.count("G") #aantal G in een sequentie
C = seq.count("C") #aantal C in een sequentie
totaal = A+T+C+G
gc =(C+G)/totaal*100 #geeft het GC%
print (totaal) #geeft het aantal nucleotiden
print (gc) # geeft het gcpercentage
