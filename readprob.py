from itertools import combinations
from networkx import Graph
from networkx.classes import graph
from networkx.classes.function import density


def readprob(path):

    graph = Graph()

    students = 0
    eggrafes = 0

    file = open(path, "r")

    lines = file.readlines()

    for line in lines:
        line = line.strip()

        if line == "":
            continue

        students += 1

        exams = line.split()

        eggrafes = eggrafes + len(exams)

        if len(exams) == 1:
            exam_int = int(exams[0])
            graph.add_node(exam_int)
            continue
        exam_comninations = combinations(exams, 2)

        for exams_a, exams_b in exam_comninations:
            exams_a_int = int(exams_a)
            exams_b_int = int(exams_b)
            graph.add_edge(exams_a_int, exams_b_int)
    density_of_graph = density(graph)

    density_rounded = round(density_of_graph, 2)
    print(f"Conflict density for {path} is {density_rounded}")
    print(f"Number of students: {students}")
    print(f"Number of enrollments: {eggrafes}")
    print(f"Number of exams: {graph.number_of_nodes()}")

    return graph


if __name__ == "__main__":
    paths = [
        "car-f-92.stu",
        "car-s-91.stu",
        "ear-f-83.stu",
        "hec-s-92.stu",
        "kfu-s-93.stu",
        "lse-f-91.stu",
        "pur-s-93.stu",
        "rye-s-93.stu",
        "sta-f-83.stu",
        "tre-s-92.stu",
        "uta-s-92.stu",
        "ute-s-92.stu",
        "yor-f-83.stu",
    ]

    for path in paths:
        graph = readprob(path)
