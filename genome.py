import feature_reader
import random
from decision_tree import DecisionTree


class Genome:
    def __init__(self, size):
        self.genes = []
        self.size = size
        self.score = 0
        self.limits = feature_reader.get_features_limits()


    def randomize(self):
        for i in range(0, self.size):
            self.genes.append(DecisionTree(6, self.limits))

    def crossover(self, p1, p2):
        for _ in range(self.size):
            if random.randint(0, 1) == 0:
                self.genes.append(p1.genes[random.randint(0, self.size - 1)])
            else:
                self.genes.append(p2.genes[random.randint(0, self.size - 1)])

    def mutate(self):
        if random.randint(0, 10) == 0:
            gene = random.randint(0, self.size - 1)
            self.genes[gene] = DecisionTree(5, self.limits)

    def decide(self, X, allowed):
        choices = [0, 0, 0, 0]
        for i in range(0, self.size):
            decision = self.genes[i].decide(X)
            # If the decision is not an "unknown state" of the tree
            if decision < len(choices):
                choices[decision] += 1
        for i in range(0, 4):
            if not allowed[i]:
                choices[i] = -1
        return choices.index(max(choices))
