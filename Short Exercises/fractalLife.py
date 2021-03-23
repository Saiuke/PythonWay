# Create a List maker

class FractalLife:
    def __init__(self, numGen: int, cellsPerGen: int, ruleSet: dict) -> object:
        """
        :rtype: object

        """
        self.mainMatrix = []
        self.numGen = numGen
        self.ruleSet = ruleSet
        self.cellsPerGen = cellsPerGen

    def __iter__(self) -> list:
        return self

    def newGen(self):
        newGenerations = []
        for _ in range(self.numGen):
            eachGen = [0] * self.cellsPerGen
            newGenerations.append(eachGen)
        for newGen in newGenerations:
            self.mainMatrix.append(newGen)
        self.plantSeed()

    def showResults(self):
        for currentLine in self.mainMatrix:
            print(' '.join(map(str, currentLine)))

    def plantSeed(self):
        middlePoint = int(round(self.cellsPerGen / 2))
        self.mainMatrix[0][middlePoint] = 1

    def changePoint(self, y, x, newValue):
        self.mainMatrix[y][x] = newValue

    def setRule(self, ruleset: dict):
        self.ruleSet = ruleset

    def create(self):
        newGen = ''
        if self.ruleSet:
            for row, currentLine in enumerate(self.mainMatrix):
                if row == self.numGen - 1:
                    break
                for column, cell in enumerate(currentLine):
                    if column == self.cellsPerGen - 2:
                        break
                    actualTrio = str(cell) + str(currentLine[column + 1]) + str(currentLine[column + 2])
                    newGen = self.ruleSet.get(actualTrio, "Rule not defined")
                    self.changePoint(row + 1, column + 1, newGen)
        else:
            print("Ruleset not defined.")

    def renderGrid(self):
        for row, currentLine in enumerate(self.mainMatrix):
            for column, cell in enumerate(currentLine):
                newValue = '\33[30m' + '○' + '\33[0m' if cell == 0 else '\33[95m' + '○' + '\33[0m'
                self.changePoint(row, column, newValue)

ruleBook = [
    {'000': 0, '001': 1, '010': 1, '011': 1, '100': 1, '101': 0, '110': 0, '111': 0},
    {'000': 0, '001': 0, '010': 1, '011': 1, '100': 1, '101': 0, '110': 0, '111': 0},
    {'000': 0, '001': 1, '010': 1, '011': 1, '100': 0, '101': 1, '110': 1, '111': 0},
    {'000': 0, '001': 1, '010': 1, '011': 0, '100': 1, '101': 1, '110': 0, '111': 1}
]

neoGenesis = FractalLife(150, 100, ruleBook[3])
neoGenesis.newGen()
neoGenesis.create()
neoGenesis.renderGrid()
neoGenesis.showResults()
