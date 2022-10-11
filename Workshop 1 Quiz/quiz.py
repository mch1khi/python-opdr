print('\n\nWelkom bij de prachtige dieren quiz van Mo\n')

antwoord = input('Ben je klaar er klaar voor? \n(ja / nee ;P):')
punten = 0
aantal_vragen = 12

if antwoord.lower() == 'ja':
    antwoord = input(
        '\nVoorafgaande vraag: kan je een paar weetjes over dieren? \n(ja / nee):')
    if antwoord.lower() == 'ja':
        punten += 1
        print(' \nYesss, dan word dit een makkie voor je!\n')
    else:
        print(' \nOeii! Hopelijk kan je een beetje gokken maatjee \n')

    antwoord = input(
        'Vraag 1: is de volgende stelling juist; legt een krokodil eieren? \n(ja / nee):')
    if antwoord.lower() == 'ja':
        punten += 1
        print(' \nLekkerr bezig! \n')
    else:
        print(' \npfffff, misschien volgende keer beter \n')

    antwoord = input(
        'Vraag 2: in welke land leven de meeste varkens? \n A Frankrijk  \n B China \n C Amerika  \n Antwoord A, B of C:')
    if antwoord.lower() == 'B':
        punten += 1
        print(' \nLekkerr bezig! \n')
    else:
        print(' \npfffff, misschien volgende keer beter \n')

    antwoord = input(
        'Vraag 3: is de volgende stelling juist; een vleermuis is geen zoogdier? \n(ja / nee):')
    if antwoord.lower() == 'nee':
        punten += 1
        print(' \nLekkerr bezig! \n')
    else:
        print(' \npfffff, misschien volgende keer beter \n')

    antwoord = input(
        'Vraag 4: Zijn er meer koeien op aarde of geiten?    \nAntwoord koeien/geiten:')
    if antwoord.lower() == 'koeien':
        punten += 1
        print(' \nLekkerr bezig! \n')
    else:
        print(' \npfffff, misschien volgende keer beter \n')

    antwoord = input(
        'Vraag 5: hoeveel weegt een tand van een olifant? \n A 4 kg  \n B 10 kg \n C 20 kg  \n Antwoord A, B of C:')
    if antwoord.lower() == 'a':
        punten += 1
        print(' \nLekkerr bezig! \n')
    else:
        print(' \npfffff, misschien volgende keer beter \n')

    antwoord = input(
        'Vraag 6: hoeveel spieren heeft een kat per oor? \n A 1  \n B 18 \n C 32 kg  \nAntwoord A, B of C:')
    if antwoord.lower() == 'c':
        punten += 1
        print(' \nLekkerr bezig! \n')
    else:
        print(' \npfffff, misschien volgende keer beter \n')

    antwoord = input(
        'Vraag 7: wat is de langste dier op aarde? \n A giraffe  \n B blauwe vinvis \n C buiskwal  \nAntwoord A, B of C:')
    if antwoord.lower() == 'c':
        punten += 1
        print(' \nLekkerr bezig! \n')
    else:
        print(' \npfffff, misschien volgende keer beter \n')

    antwoord = input(
        'Vraag 8: welke kleur hebben kaketoes meestal?  \nAntwoord:')
    if antwoord.lower() == 'wit':
        punten += 1
        print(' \nLekkerr bezig! \n')
    else:
        print(' \npfffff, misschien volgende keer beter \n')


def diereninfo(antwoord):
    big5 = ['olifant', 'leeuw', 'nijlpaard', 'luipaard', 'neushoorn']
    for dier in big5:
        if dier == antwoord.lower():
            return True
        else:
            return False


antwoord = input(
    'Vraag 9: noem een dier uit de big 5?  \nAntwoord:')
if antwoord.lower() == diereninfo(True):
    punten += 1
    print(' \nLekkerr bezig! \n')
else:
    print(' \npfffff, misschien volgende keer beter \n')


antwoord = input(
    'Vraag 10: noem nog een dier uit de big 5?  \nAntwoord:')
if antwoord.lower() == diereninfo(antwoord):
    punten += 1
    print(' \nLekkerr bezig! \n')
else:
    print(' \npfffff, misschien volgende keer beter \n')


# print('\n\nBedankt voor het spelen van de Quiz, je hebt '+str(punten) +
#       ' van de '+str(aantal_vragen)+' vragen juist beantwoord!')
# cijfer = round(float(10/aantal_vragen*punten), 1)
# print('Je cijfer voor project komt daarmee op een voorlopige '+str(cijfer)+'.')
# if punten >= 2:
#     print('Goed bezig!')
# else:
#     print('Hmmm, kan beter... nog even oefenen chef.\n\n')
