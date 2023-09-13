import random  # importera random modul för att blanda kortleken
from kort import Kortlek
from spelare import Spelare


class TjugoettSpel:  # börjar på tjogoettklass
    def __init__(self):
        self.kortlek = Kortlek()

    def starta(self):
        # säger till spelaren välkommen och hälsning
        print("Välkommen till Tjugoett!")
        print("Vi önskar dig stort lycka till, du kommer behöva det!")

# det här är en huvudloop där spelaren kan välja att starta eller avsluta gamet, jag har använt ja och nej för att kolla detta
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
        # skapa en ny spelare och dealer varje omgång
        spelare = Spelare()
        dealer = Spelare()

        # delar ut 2 kort var till spelare och dealer
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

        # dealern drar kort tills den har minst 17 som vanligt i kortspel
        while dealer.rakna_poang() < 17:
            dealer.drakort(self.kortlek.dra_kort())

        #  visar resultat för spelare och dealer
        print(f"Din hand: {spelare.visa_hand()}, Poäng: {spelare.rakna_poang()}")
        print(f"Dealerns hand: {dealer.visa_hand()}, Poäng: {dealer.rakna_poang()}")
        # kollar resultatet och vem som vinner
        if spelare.rakna_poang() > 21:
            print("Dealern vinner. Du har över 21 poäng. (BUST)")
        elif dealer.rakna_poang() > 21 or spelare.rakna_poang() > dealer.rakna_poang():
            print("Grattis! Du vinner! Hur gjorde du detta?")
        elif spelare.rakna_poang() == dealer.rakna_poang():
            print("Huset vinner tyvärr! Lycka till nästa gång.")
        else:
            print("Dealern vinner. Du kanske borde prova ett annat spel?")


# skapar spelobjektet
spel = TjugoettSpel()
# startat spelet
spel.starta()
