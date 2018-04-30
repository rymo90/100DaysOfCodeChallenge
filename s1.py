# coding: utf-8
########################################################################
# Mall för labb S1, DD1361 Programmeringsparadigm.
# Författare: Per Austrin
########################################################################

########################################################################
# Dessa funktioner är det som ska skrivas för att lösa de olika
# uppgifterna i labblydelsen.
########################################################################

def dna():          # uppgift 1
    # matcha  sträng endas om det består av ACGT bokstäver ett frit antal gånger.
    return "(^[ACGT]+$)"

def sorted():       # uppgift 2
    # match stängen ändas om det är tal som är avstigande ordning.
    return "^9*8*7*6*5*4*3*2*1*0*$"

def hidden1(x):     # uppgift 3
    # indata x är strängen som vi vill konstruera ett regex för att söka efter
    #den kollar vänster och höger sidan av given text för att kolla om det matchar med x.
    return "((?<=[a-zA-Z0-9]))?"+x+"((?=[a-zA-Z0-9]))?"
def hidden2(x):     # uppgift 4
    # indata x är strängen som vi vill konstruera ett regex för att söka efter
    # y värde har * teken mellan x element. detta kommer att hjälpa att hitta
    #texten som finns i given text.
    y= ".*?".join(x)
    # return y
    return  "((?<=[a-zA-Z0-9]))?"+y+"((?=[a-zA-Z0-9]))?"
def equation():     # uppgift 5
    # vi har = teken som förekommer en eller noll gång. vänser sidan av det teken
    # har vi decimal tal med obegräsad antal och kan förekomma som +/-
    # höger sidan av = har vi aritimetisk teken samt decimal nummer med obgärndas antal
    return "^(([+-]?[0-9]+)+[=]?([+*/-]?[0-9]+)+)+$"
def parentheses():  # uppgift 6
    # fem parenthese fall,  som kollar på djupet av paranthese
    # en hårdkodat kod. för att uppgiften begränsad till max fem fördjupning
    return "^(\((\((\((\((\(\))*\))*\))*\))*\))*$"
def sorted3():      # uppgift 7
    return "^\d*(([0-7]89)|([0-6]7[8-9])|([0-5]6[7-9]|([0-4]5[6-9])|([0-3]4[5-9])|([0-2]3[4-9])|([0-1]2[3-9])|(01[2-9]))+)\d*$"
########################################################################
# Raderna nedan är lite testkod som du kan använda för att provköra
# dina regexar.  Koden definierar en main-metod som läser rader från
# standard input och kollar vilka av de olika regexarna som matchar
# indata-raden.  För de två hidden-uppgifterna används söksträngen
# x="test" (kan lätt ändras nedan).  Du behöver inte sätta dig in i hur
# koden nedan fungerar om du inte känner för det.
#
# För att provköra från terminal, kör:
# $ python s1.py
# Skriv in teststrängar:
# [skriv något roligt]
# ...
########################################################################
from sys import stdin
import re
def main():
    def hidden1_test(): return hidden1('progp')
    def hidden2_test(): return hidden2('progp')
    tasks = [dna, sorted, hidden1_test, hidden2_test, equation, parentheses, sorted3]
    print('Skriv in teststrängar:')
    while True:
        line = stdin.readline().rstrip('\r\n')
        if line == '': break
        for task in tasks:
            result = '' if re.search(task(), line) else 'INTE '
            print('%s(): "%s" matchar %suttrycket "%s"' % (task.__name__, line, result, task()))

if __name__ == '__main__': main()
