import sys
import shidoku
from src.genetic.individual import Individual
from src.genetic.selection import selection_roullete

args = sys.argv
pop_size = 500
max_generations = 50

def generate_initial_population(puzzle):
    population = []
    for _ in range(pop_size):
        individual = Individual(puzzle)
        population.append(individual)

    return population

def display_info(population):
    for i, individual in enumerate(population):
        print(f"Individual {i+1}:")
        print("Chromosome:", individual.chromosome)
        print("Fitness:", individual.fitness)
        individual.print_info()
        print()

def main():
    with open(args[1], 'r') as arq:
        puzzle_string = arq.read()

    print("Selected puzzle:", puzzle_string)
    print("Population size:", pop_size)
    print()

    puzzle = shidoku.string_to_array(puzzle_string)
    population = generate_initial_population(puzzle)

    verification = False
    individual_with_fitness_36 = None

    while not verification:
        for individual in population:
            if individual.fitness == 36:
                individual_with_fitness_36 = individual
                verification = True
                break
        else:
            if individual_with_fitness_36 is not None:
                print("Individual wiht fitness = 36 not found:")
                print("Chromosome:", individual_with_fitness_36.chromosome)
                print("Fitness:", individual_with_fitness_36.fitness)
                individual_with_fitness_36.print_info()

            selection_roullete(population)

if __name__ == '__main__':
    main()