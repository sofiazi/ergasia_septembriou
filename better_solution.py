from networkx import Graph
import networkx as nx

def color_dsatur(graph: Graph):
    solution = dict()
    solution = nx.coloring.greedy_color(graph, strategy="DSATUR")
    return solution

def better_solution (problem_name, solution, periods):
    name_without_suffix = problem_name.replace(".stu","" )
    save_name = f"{name_without_suffix}_{periods}.sol"
    with open(save_name, "w") as file:
        for key in solution:
            file.write(f"{key}\t{solution[key]}\n")