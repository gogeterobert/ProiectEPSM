from ProfilEnergie import ProfilEnergie


class Drona:
    def __init__(self, baterii, greutateDrona, profilEnegieMotoare):
        self.greutateDrona = greutateDrona
        self.baterii = baterii
        self.profilEnergieMotoare = ProfilEnergie(profilEnegieMotoare)

    def calculeazaTimpFaraEsalonare(self):
        greutateTotala = self.iaGreutateTotalaDrona()
        intensitateCurent = self.profilEnergieMotoare.profil[greutateTotala]
        return self.iaCapacitateToalaBaterii() / intensitateCurent

    def calculeazaTimpCuEsalonare(self):
        timp = 0
        while(self.baterii):
            baterie = self.baterii.pop()
            greutateTotala = self.iaGreutateTotalaDrona()
            intensitateCurent = self.profilEnergieMotoare.profil[greutateTotala]
            timp += baterie['capacitate'] / intensitateCurent
        return timp

    def iaCapacitateToalaBaterii(self):
        capacitate = 0
        for baterie in self.baterii:
            capacitate += baterie['capacitate']
        return capacitate

    def iaGreutateTotalaDrona(self):
        greutate = self.greutateDrona
        for baterie in self.baterii:
            greutate += baterie['greutate']
        return greutate

    def iaNumarBaterii(self):
        return len(self.baterii)
