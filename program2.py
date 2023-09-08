# Skapa ett program där användaren får mata in två tal. 
# Låt sedan programmet skriva ut alla tal som finns mellan dessa två tal på skärmen. 
# Lös detta med en for-loop. Lös den igen med en While-loop

num1 = int(input('Skriv in första heltal: '))
num2 = int(input('Skriv in andra heltal: '))
# Ta in 2 heltal
# Därefter måste vi veta vilken som är störst och minst
# Därefter kan vi stega från det minsta till det största
if  num1 > num2: # ----> Då vet vi att (num1 + 1) >= num2
    # -----------------------------------
    # Om vi kommer hit så vet vi:
    största = num1
    minsta = num2
    # -----------------------------------
    tal_i_mellan = minsta + 1

    while tal_i_mellan < största:
        print(tal_i_mellan)
        tal_i_mellan+=1

elif num2 > num1:
    # -----------------------------------
    # Om vi kommer hit så vet vi:
    största = num2
    minsta = num1
    # -----------------------------------
else:
    # Talen är lika och inget ska skrivas ut
    pass