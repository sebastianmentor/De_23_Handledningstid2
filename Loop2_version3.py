# Skapa ett program där användaren får mata in två tal. 
# Låt sedan programmet skriva ut alla tal som finns mellan dessa två tal på skärmen. 
# Lös detta med en for-loop. Lös den igen med en While-loop
#----------------------------------------------------------------------------------
# Steg 1. Ta in 2 heltal (kontroll om man vill)
# Steg 2. Därefter måste vi veta vilken som är störst och minst
# Steg 3. Därefter kan vi stega från det minsta till det största


num1 = int(input('Skriv in första heltal: ')) 
num2 = int(input('Skriv in andra heltal: '))

störst = max(num1,num2)
minsta = min(num1,num2)

minsta +=1

if störst-minsta > 0:
    while minsta < störst:
        print(minsta)
        minsta += 1