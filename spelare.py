class Spelare:
    def __init__(self):
        self.hand = []  # skapad en tom hand för spelaren alltså jag som är spelare

    def drakort(self, kort):
        self.hand.append(kort)  # lägger till kort i spelarens hand

    def rakna_poang(self):
        poang = sum(self.hand)  # räkna poäng genom att sumera värden i handen
        if 14 in self.hand and poang > 21:
            self.hand.remove(14)
            self.hand.append(1)  # om jag har ett S som är 14 och det går över 21 då räknas det som 1 istället
            poang = sum(self.hand)
        return poang

    def visa_hand(self):
        return " : ".join(map(str, self.hand))  # konverterar till sträng för att visa kort annars går det ej
