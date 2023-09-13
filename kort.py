import random  # importera random modul för att blanda kortleken

class Kortlek:
    def __init__(self):
        # skapa en ny kortlek, genom att multiplicera varje kortvärde med 4 hjärter ruter klöver och spader
        self.kortlek = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 14] * 4  # här har jag lagt in s som 14
        random.shuffle(self.kortlek)  # blanda kortleken vid skapandet.

    def dra_kort(self):
        return self.kortlek.pop()  # dra kort från kortlek och retunera det in
