import random

class Individual:
    def __init__(self, puzzle) -> None:
        self.chromosome = self.generate_chromosome(puzzle) 
        self.calculate_fitness()

    def generate_chromosome(self, puzzle) -> list[int]:
        chromosome = []
        for row in puzzle:
            new_row = []
            for val in row:
                if val == 0:
                    val = random. randint(1, 4)
                new_row.append(val)
            chromosome.append(new_row)
        return chromosome

    def define_chromosome(self, genes) -> None:
        self.chromosome = genes
        self.calculate_fitness()

    def calculate_fitness(self) -> None:
        num = 36
        total_errors = 0 
        errors_in_rows = []
        errors_in_columns = []
        errors_in_quadrants = []

        for row in self.chromosome:
            rows_without_duplicates = set(row)
            errors_in_row = len(row) - len(rows_without_duplicates)
            total_errors += errors_in_row
            errors_in_rows.append(errors_in_row)

        columns = zip(*self.chromosome)
        for column in columns:
            column_without_duplicates = set(column)
            errors_in_column = len(column) - len(column_without_duplicates)
            total_errors += errors_in_column
            errors_in_columns.append(errors_in_column)

        for i in range(0, 4, 2):
            for j in range(0, 4, 2):
                quadrant = [row[j:j + 2] for row in self.chromosome[i:i + 2]]
                quadrants_without_duplicates = set(row for subgrid in quadrant for row in subgrid)
                errors_in_quandrant = len(quadrant) * 2 - len(quadrants_without_duplicates)
                total_errors += errors_in_quandrant
                errors_in_quadrants.append(errors_in_quandrant)

        self.fitness = num - total_errors
        self.errors_in_rows = errors_in_rows
        self.errors_in_columns = errors_in_columns
        self.errors_in_quadrants = errors_in_quadrants

    def print_info(self) -> None:
        print("Errors in rows:", self.errors_in_rows)
        print("Errors in columns:", self.errors_in_columns)
        print("Errors in quadrants:", self.errors_in_quadrants)
        print()