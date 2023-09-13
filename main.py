import random  # importera random modul för att blanda kortleken


class Kortlek:
    def __init__(self):
        # skapa en ny kortlek, genom att multiplicera varje kortvärde med 4 hjärter ruter klöver och spader
        self.kortlek = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 14] * 4  #här har jag lagt in s som 14
        random.shuffle(self.kortlek)  # blanda kortleken vid skapandet.

    def dra_kort(self):
        return self.kortlek.pop()  # dra kort från kortlek och retunera det in


class Spelare:
    def __init__(self):
        self.hand = []  # skapad en tom hand för spelaren alltså jag som är spelare

    def drakort(self, kort):
        self.hand.append(kort)  # lägger till kort i spelarens hand

    def rakna_poang(self):
        poang = sum(self.hand)  # räkna poäng genom att sumera värderna i handen
        if 14 in self.hand and poang > 21:
            self.hand.remove(14)
            self.hand.append(1)  # om jag har ett S som är 14 och det går över 21 då räknas det som 1 istället
            poang = sum(self.hand)
        return poang

    def visa_hand(self):
        return " : ".join(map(str, self.hand))  # konverterar till sträng för att visa kort annars går det ej


class TjugoettSpel: # börjar på tjogoettklass
    def __init__(self):
        self.kortlek = Kortlek()


