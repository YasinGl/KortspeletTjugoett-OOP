import random  # importera random modul för att blanda kortleken


class Kortlek:
    def __init__(self):
        # skapa en ny kortlek, genom att multiplicera varje kortvärde med 4 hjärter ruter klöver och spader
        self.kortlek = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 14] * 4  # här har jag lagt in s som 14
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


class TjugoettSpel:  # börjar på tjogoettklass
    def __init__(self):
        self.kortlek = Kortlek()

    def starta(self):
        # säger till spelaren välkommen och hälsning
        print("Välkommen till Tjugoett!")
        print("Vi önskar dig stort lycka till, du kommer behöva det!")

# det här är en huvudloop där spelaren kan välja att starta eller avsluta gamet
        while True:
            # här frågar jag spelare om man vill spela eller inte
            val = input("Starta spel? Ja/Nej?: ").lower()

            # svar ja då kommer spelet starta
            if val == "ja":
                self.spela()
            # om spelaren säger nej så tar programmet slut
            elif val == "nej":
                print("Hej då!")
                break
            # fel hantering om man svarar nåt helt annat
            else:
                print("Vänligen svara JA eller NEJ!")

    def spela(self):
        # skapa en ny spelare och delaer varje omgång
        spelare = Spelare()
        dealer = Spelare()

        # delar ut 2 kort var till seplare och dealer
        for _ in range(2):
            spelare.drakort(self.kortlek.dra_kort())
            dealer.drakort(self.kortlek.dra_kort())

   # gamet börjar nu kan spelaren välja om man vill dra ett kort eller stanna
        while True:
            # visar hand och poäng
            print(f"Din hand: {spelare.visa_hand()}, Poäng: {spelare.rakna_poang()}")
            # visar dealer första kort ,en den andra är dold
            print(f"Dealerns hand: {dealer.hand[0]} _")
            # frågar spelaren vad den vill göra dra kort eller ej
            val = input("Vill du dra ett kort? (J/N): ").lower()
            if val == "j":
                # drar kort från leken till spelarens hand
                spelare.drakort(self.kortlek.dra_kort())
                # kollar om spelaren har fått över 21 poäng
                if spelare.rakna_poang() > 21:
                    print(f"Din hand: {spelare.visa_hand()}, Poäng: {spelare.rakna_poang()}")
                    print("Du har över 21 poäng. Du förlorar.")
                    break
            else:
                # avsluta gamet om spelaren väljer att inte dra fler kort
                break

