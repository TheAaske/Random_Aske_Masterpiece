# Her importerer jeg random modulet som kan vælge tal tilfældigt(til en hvis grad)
import random

# Jeg laver her en funktion med et for loop som tjekker hvor mange elementer der er i lister for de forskellige karakter jeg har lavet længere nede
def bestikkelse(genstande):
    chance = 0
    for i in genstande:
        chance += 25 # for hver element i en liste tilføjer jeg en værdi som senere bliver brugt ttil at udregne chancen for at bestikke "ridderen"
    return chance 

# Denne funktion bliver brugt flere gange når man kommer til et sted hvor man er død eller har gennemført spillet
def gameover(restart):
    if restart == 'ja': # den får svaret ind fra et argument og laver det om til et tal som så bliver brugt i resten af koden
        return 1
    elif restart == 'nej':
        return 2

# Dette er "Main"-koden af spillet, denne er lagt ind i et "while True:" for at jeg kan køre break eller continue for at styre om jeg skal slutte spillet eller starte forfra
while True:
    # indledende tekst
    print("\n\n\nVelkommen til spillet RAM (Random Aske Masterpiece)\n\n")
    
    print("1. Wizard")
    print("2. Warrior")
    print("3. Ranger")
    # Her skal brugeren indtaste et karaktervalg og i en "while True:" for at sikre at brugeren ikke kan går videre uden at skrive en af valgmulighederne
    while True:
        classValg = input("\nVælg en class ved at skrive nummeret der passer til:\n")
        if classValg == '1' or classValg == '2' or classValg == '3': # hvis en af valgmulighederne passer med inputtet fra brugeren går den videre med koden, 
            break                                                       # ellers prøver man igen i uendelighed
        else:
            continue

    # Her kan brugeren frit skrive hvilket som helst som navn 
    name = input("Giv din karakter et navn:\n")
    
    # Her definerer jeg efter hvilken karakter brugeren vælger våbenskade og hvilke og hvor mange ting de hver især har
    if classValg == '1':
        våbenDmg = 20
        genstande = ['Magisk ring']
    elif classValg == '2':
        våbenDmg = 15
        genstande = ['Elver halskæde','Pose guldmønter']
    elif classValg == '3':
        våbenDmg = 10
        genstande = ['Elver smykker','Pose guldmønter','Arkenstone']

    # Jeg har lagt en masse historie-tekst ind med inputs for at lave mellemrum så det hele ikke kommer med det samme
    print("\n\n\nVelkommen til Midgård " + name)
    input("(Tryk enter)\n\n")

    print("Du er sat på en mission for at redde Midgård fra det onde")
    print("Held og lykke på rejsen, værsgo at starte")
    input("(Tryk enter)\n\n")

    print("Der er nu gået noget tid og du har nu reddet langt og er kommet til et sted kaldet Rohan")
    input("(Tryk enter)\n\n")
    print("Her ser du en ridder iført en sort rustning\n")
    print("Ridder: Holdt! ingen må passere ind til riget Mordor! Forsvind eller dø!")
    input("(Tryk enter)\n\n")

    print("Hvad vil du gøre her?\n")
    print("1. bestik ham")
    print("2. Kæmp mod ham\n")

    # Her vælges hvad handling der skal ske ved ridderen, også sikret mod forkerte input med "while True:"
    while True:
        ridderValg = input("skriv nummeret på dit valg\n")
        if ridderValg == '1' or ridderValg == '2':
            break
        else:
            continue

    if ridderValg == '1':
        print("For bestikke ham skal du give ham dine genstande.")
        print("Du har " + str(len(genstande)) + " genstande på dig")
        input("(Tryk enter)\n")
        print("Derudover bestemmer han om det er nok.")
        input("(Tryk enter)\n")
        
        # Her kalder jeg random funktion for at få et random heltal i det range jeg har angivet og gemmer det i en variabel
        randTal = random.randint(1, 10)
        
        # Her bestemmes der på bagrund af det random tal om chancen fra den første funktion skal være højere eller lavere og gemmer det i en variabel
        if randTal >= 5:
            genstandOk = bestikkelse(genstande) + 25
        elif randTal < 5:
            genstandOk = bestikkelse(genstande) - 25

        # Her brugsen den chance så alt efter om den er for lav eller for høj til at bestemme om man kan går videre eller ej.
        if genstandOk < 50:
            print("Han er ikke tilfreds. Så han slog dig ihjel...")
            
            # Her bliver den anden funktion brugt for at spørge om brugeren vil prøve igen efter død
            while True:
                forfra = input("Vil du starte forfra (ja/nej)\n")
                if forfra == 'ja' or forfra == 'nej':
                    break
                else:
                    continue
            
            # Kalder gameover funktionen og bruger inputtet "forfra" som argument
            svar = gameover(forfra)
            if svar == 1: # Bruger returproduktet fra gamover funktionen til at få svar 1 eller 2
                continue
            elif svar == 2:
                break
        elif genstandOk >= 50:
            print("Du fik bestukket ham. Du kan nu fortsætte ind i Mordor\n")
            pass # Bruger her "Pass" til at gå videre til næste kode-del udenfor dette while-loop
    
    # Her er det andet valg hvor jeg istedet kæmper mod ridderen og her bruger våbenskade som defineret tidligere sammen med det random tal til at bestemme kampens udfald
    elif ridderValg == '2':
        
        # Definerer igen et random heltal men med et andet range
        randTal = random.randint(1, 100)
        print("\n\nDu har valgt at kæmpe mod ham.")
        print("Et terninge-kast vil bestemme om dit angreb skader nok")
        input("(Angrib!)\n")
        
        # Her bestemmes om der skal tilføjes eller fjernes skade fra våben på baggrund af det random heltal
        if randTal >= 50:
            ridderSkade = våbenDmg + 50
        elif randTal < 50:
            ridderSkade = våbenDmg - 10
        
        # Så bestemmes om karakterens angreb vinder på baggrund af den nye udregnede våbenskade
        if ridderSkade < 50:
            print("Dit angreb var ikke stærkt nok, ridderen slog dig ihjel...")
            
            # igen sikres der at der kun bliver skrevet ja eller nej ved spørgsmål om at prøve igen
            while True:
                forfra = input("Vil du starte forfra (ja/nej)\n")
                if forfra == 'ja' or forfra == 'nej':
                    break
                else:
                    continue
            svar = gameover(forfra)
            if svar == 1:
                continue
            elif svar == 2:
                break
        elif ridderSkade >= 50:
            print("Dit angreb slog ridderen ihjel, du kan nu fortsætte ind i Mordor.")
            input("(Tryk enter)\n")
            pass # Igen bruges pass til at gå videre fra det while-loop det er i
    
    # Historisk tekst igen med inputs for pauser
    print("Du har nu forladt Rohan og er på vej ind i Mordor")
    input("(Tryk enter)")

    print("\n\n\nI Mordor ser du en stor vulkan med en åbning til et rum i toppen af den.")
    print("Inde i rummet bliver du mødt af et stort monster, en Balrog!\n")
    print("Den blokerer døren bag dig med et slag mod væggen og går hen mod dig for at kæmpe mod dig.\n")

    print("Hvordan vil du håndtere Balroggen?\n")
    print("1. Kæmp mod Balroggen")
    print("2. Flygt!\n")

    # Her er det næste valg om at kæmpe mod balrog eller ej, dette er også sikret mod at skrive andet end 1 og 2
    while True:
        balrogValg = input("Skriv nummeret på dit valg og tryk enter\n")
        if balrogValg == '1' or balrogValg == '2':
            break
        else:
            continue

    #Jeg definerer bossens liv her for at jeg kan bruge variablen i et globalt scope for de næste statements
    balrogLiv = 100

    # Her vælges selve kamp-sekvensen, sat op på samme måde som de forrige dele af koden med "while True:" og nestede if-statements, men her har jeg fortsat det 3 gange.
    if balrogValg == '1':
        print("\nDu har valgt at kæmpe mod Balroggen")
        print("Du har tre forsøg til at slå den ihjel, ellers slår den dig ihjel...")
        print("Bossen har 100 liv, dit våben bestemmer skaden, men for hver tur kan der forekomme en random buff eller debuff\n")

        # Slag nummmer 1
        print("Slag 1")
        print("Balrog liv: " + str(balrogLiv))
        print("1. Normal attack")

        # Jeg har indført at der kan vælges et heavy slag som bare tilføjer 30 til værdien af våbenskade. 
        # Dette afhænger dog stadig af det random heltal og våbnets oprindelige skade
        print("2. Heavy attack (+30dmg)")

        # Sikring af forkert input med "while True:"
        while True:
            attack1Input = input("Skriv nummer på valg af angreb\n")
            if attack1Input == '1' or attack1Input == '2':
                break
            else:
                continue
        randTal = random.randint(1, 100)

        # Tilføjer eller trækker våbenskade fra ved slag alt efter random heltal
        if randTal >= 50:
            attack1 = våbenDmg + 30
        elif randTal < 50:
            attack1 = våbenDmg - 5

        # Her beregnes hvor meget våbenskade der bruges eller tilføjes (buff/debuff) balroggens liv på baggrund af det liv den har nu og våbenskade for nuværende slag
        if attack1Input == '1':
            balrogLiv = balrogLiv - attack1
        elif attack1Input == '2':
            attack1 = attack1 + 30
            balrogLiv = balrogLiv - attack1
        
        # Her og efter de andre slag tjekker jeg balroggens liv (variabel-værdi) for at se om spillet kan afsluttes endnu eller startes forfra ellerr fortsætte
        if balrogLiv <= 0:
            print("\nDu dræbte Balroggen og reddede Midgård")
            print("Her er en smiley som præmie :D\n")
            while True:
                forfra = input("Vil du starte forfra (ja/nej)\n")
                if forfra == 'ja' or forfra == 'nej':
                    break
                else:
                    continue
            svar = gameover(forfra)
            if svar == 1:
                continue
            elif svar == 2:
                break
        elif balrogLiv > 0:
            pass
        
        # Slag 2
        print("\nSlag 2")
        print("Balrog liv: " + str(balrogLiv))
        print("1. Normal attack")
        print("2. Heavy attack (+30dmg)")

        # Sikring af forkert input med "while True:"
        while True:
            attack2Input = input("Skriv nummer på valg af angreb\n")
            if attack2Input == '1' or attack2Input == '2':
                break
            else:
                continue
        randTal = random.randint(1, 100)

        # Tilføjer eller trækker våbenskade fra ved slag alt efter random heltal
        if randTal >= 50:
            attack2 = våbenDmg + 30
        elif randTal < 50:
            attack2 = våbenDmg - 5
        
        # Her beregnes hvor meget våbenskade der bruges eller tilføjes (buff/debuff) balroggens liv på baggrund af det liv den har nu og våbenskade for nuværende slag
        if attack2Input == '1':
            balrogLiv = balrogLiv - attack2
        elif attack2Input == '2':
            attack2 = attack2 + 30
            balrogLiv = balrogLiv - attack2

        # Her ser jeg på at hvis balroggen ikke har mere liv har jeg vundet og kan starte forfra igen eller slutte spillet
        if balrogLiv <= 0:
            print("\nDu dræbte Balroggen og reddede Midgård")
            print("Her er en smiley som præmie :D\n")
            while True:
                forfra = input("Vil du starte forfra (ja/nej)\n")
                if forfra == 'ja' or forfra == 'nej':
                    break
                else:
                    continue
            svar = gameover(forfra)
            if svar == 1:
                continue
            elif svar == 2:
                break
        elif balrogLiv > 0:
            pass

         # Slag 3
        print("\nSlag 3")
        print("Balrog liv: " + str(balrogLiv))
        print("1. Normal attack")
        print("2. Heavy attack (+30dmg)")

        # Sikring af forkert input med "while True:"
        while True:
            attack3Input = input("Skriv nummer på valg af angreb\n")
            if attack3Input == '1' or attack3Input == '2':
                break
            else:
                continue
        randTal = random.randint(1, 100)

        # Tilføjer eller trækker våbenskade fra ved slag alt efter random heltal
        if randTal >= 50:
            attack3 = våbenDmg + 30
        elif randTal < 50:
            attack3 = våbenDmg - 5
        
        # Her beregnes hvor meget våbenskade der bruges eller tilføjes (buff/debuff) balroggens liv på baggrund af det liv den har nu og våbenskade for nuværende slag
        if attack3Input == '1':
            balrogLiv = balrogLiv - attack3
        elif attack3Input == '2':
            attack3 = attack1 + 30
            balrogLiv = balrogLiv - attack3

        # Her ser jeg på at hvis balroggen ikke har mere liv har jeg vundet og kan starte forfra igen eller slutte spillet
        if balrogLiv <= 0:
            print("\nDu dræbte Balroggen og reddede Midgård")
            print("Her er en smiley som præmie :D\n")
            while True:
                forfra = input("Vil du starte forfra (ja/nej)\n")
                if forfra == 'ja' or forfra == 'nej':
                    break
                else:
                    continue
            svar = gameover(forfra)
            if svar == 1:
                continue
            elif svar == 2:
                break
        elif balrogLiv > 0:
            pass
        
        # Her tjekker jeg for om at hvis balroggen stadig har liv så vil man have tabt og man har mulighed for at starte forfra igen
        if balrogLiv > 0:
            print("\nDu nåede ikke at dræbe Balroggen før den dræbte dig!")
            print("You Died!\n")

            while True:
                forfra = input("Vil du starte forfra (ja/nej)\n")
                if forfra == 'ja' or forfra == 'nej':
                    break
                else:
                    continue
            svar = gameover(forfra)

            if svar == 1:
                continue
            elif svar == 2:
                break
    
    # Hvis brugeren ikke vælger at kæmpe mod balroggen vælges her den anden mulighed hvor man bare dør med det samme og kan vælge at starte forfra eller slutte spiller
    elif balrogValg == '2':
        print("\nDu vælger at flygte og løber ud over kanten og direkte ned i lavaen...")
        print("You Died!\n")
        while True:
            forfra = input("Vil du starte forfra (ja/nej)\n")
            if forfra == 'ja' or forfra == 'nej':
                break
            else:
                continue
        svar = gameover(forfra)
        if svar == 1:
            continue
        elif svar == 2:
            break