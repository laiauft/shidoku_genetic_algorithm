import random
from typing import List
from genetic.individual import Individual

def selection_roullete(population: List[Individual]) -> Individual:
    total_fitness = sum(individual.fitness for individual in population)
    limit = random.uniform(0, total_fitness)
    accumulated = 0
		
    for individual in population:
        accumulated += individual.fitness
        if accumulated >= limit:
            return individual