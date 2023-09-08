# Skapa ett program där användaren får mata in två tal. 
# Låt sedan programmet skriva ut alla tal som finns mellan dessa två tal på skärmen. 
# Lös detta med en for-loop. Lös den igen med en While-loop
#----------------------------------------------------------------------------------
# Steg 1. Ta in 2 heltal (kontroll om man vill)
# Steg 2. Därefter måste vi veta vilken som är störst och minst
# Steg 3. Därefter kan vi stega från det minsta till det största


num1 = int(input('Skriv in första heltal: ')) 
num2 = int(input('Skriv in andra heltal: '))

if  num1 > num2: # ----> Då vet vi att (num1 + 1) >= num2
    # -----------------------------------
    # Om vi kommer hit så vet vi:
    största = num1
    minsta = num2
    # -----------------------------------
    # Vi lägger till 1 på det minsta talet då det kommer vara 
    # det första talet som vi vill skriva ut om det "finns" 
    # tal mellan största och minsta talen
    tal_i_mellan = minsta + 1 

    # Vi jämnför om det finns tal mellan som ska skrivas ut 
    # och om så fallet så hoppar vi in i loopen och skriver ut
    # det talet, stegar ett steg till och kontrollerar om nästa 
    # tal i talföljden ska skrivas ut!
    while tal_i_mellan < största: 
        print(tal_i_mellan)
        tal_i_mellan+=1

elif num2 > num1:
    # -----------------------------------
    # Om vi kommer hit så vet vi:
    största = num2
    minsta = num1
    # -----------------------------------
    # Vi lägger till 1 på det minsta talet då det kommer vara 
    # det första talet som vi vill skriva ut om det "finns" 
    # tal mellan största och minsta talen
    tal_i_mellan = minsta + 1 
    # Vi jämnför om det finns tal mellan som ska skrivas ut 
    # och om så fallet så hoppar vi in i loopen och skriver ut
    # det talet, stegar ett steg till och kontrollerar om nästa 
    # tal i talföljden ska skrivas ut!
    while tal_i_mellan < största:
        print(tal_i_mellan)
        tal_i_mellan+=1
else:
    # Talen är lika och inget ska skrivas ut
    pass