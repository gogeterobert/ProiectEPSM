import sys
from Drona import Drona
import help
import json

def incarcaFisierDate(filePath):
    f = open(filePath, "r")
    return f.read()

def main():
    date = incarcaFisierDate(sys.argv[1])
    dateJson = json.loads(date)

    drona = Drona(**dateJson)

    numarBaterii = drona.iaNumarBaterii()

    timpNeoptimizat = drona.calculeazaTimpFaraEsalonare()
    timpOptimizat = drona.calculeazaTimpCuEsalonare()
    optimizare = (timpOptimizat - timpNeoptimizat) / timpNeoptimizat
    
    print("Optimizare de: " + str("{:.2f}".format(optimizare * 100)) + "%")

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        help.showHelp()
        sys.exit()
    
    main()
