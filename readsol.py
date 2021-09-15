from networkx import Graph


def readsol(path):
    solution = dict()

    file = open(path, "r")

    lines = file.readlines()

    for line in lines:
        line = line.strip()
        line_contains = line.split()
        exam = int(line_contains[0])
        period = int(line_contains[1])
        solution[exam] = period

    return solution


def evaluate(graph: Graph, solution):
    used_periods = dict()
    for node in graph:
        if node not in solution.keys():
            print(f"Λείπει η εξέταση {node}")
            return 0, False
        assigned_period = solution[node]
        if assigned_period < 0:
            print(f"H εξέταση {node} έχει αρνητικό αριθμό")
            return 0, False
        used_periods[assigned_period] = True

    for node_a, node_b in graph.edges():
        if solution[node_a] == solution[node_b]:
            print(f"H εξέταση {node_a} έχει σύγκρουση με εξέταση {node_b} ")
            return 0, False

    return len(used_periods), True
