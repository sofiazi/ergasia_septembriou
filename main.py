from os import path
from networkx.classes import graph
from readprob import readprob
from readsol import readsol, evaluate
from better_solution import better_solution, color_dsatur

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
graph = 0

while True:
    print("MENOY - Επιλογή από 0 έως 4")
    print("0 - ΕΞΟΔΟΣ")
    print("1 - Επιλογή φόρτωσης προβλήματος")
    print("2 - Επιλογή διάβασμα λυσης")
    print("3 - Επιλογή επίλυσης προβλήματος")
    print("4 - Επιλογή μαζικής λύσης")
    user_input = input("Πληκτρολόγησε μια ειλογή απο το μενού: ")
    user_input_integer = int(user_input)

    if user_input_integer == 0:
        break
    elif user_input_integer == 1:
        print("Επέλεξε τον φάκελο του προβλήματος: ")
        for index, path in enumerate(paths):
            print(index, path)
        i = input("Εισαγωγή προβλήματος: ")
        problem = paths[int(i)]
        graph = readprob(problem)

    elif user_input_integer == 2:
        if graph == 0:
            print("Δεν επιλέχτηκε κάποιο πρόβλημα.")
            print()
            continue
        else:
            print("Επιλέξετε αρχείο προβλήματος: ")
            solution_file = input("Εισαγωγή προβλήματος:")
            solution_dictionary = readsol(solution_file)
            periods_used, valid_coloring = evaluate(graph, solution_dictionary)
            if valid_coloring == True:
                print(f"Εγκυρη λύση, χρησιμοποιηθηκαν {periods_used} περιοδοι.")
            else:
                print("Άκυρη λύση")

    elif user_input_integer == 3:
        if graph == 0:
            print("Δεν επιλέχτηκε κάποιο πρόβλημα.")
            print()
            continue
        else:
            coloring = color_dsatur(graph)
            periods_used, valid_coloring = evaluate(graph, coloring)
            if valid_coloring:
                print("Found S1olution")
                better_solution(problem, coloring, periods_used)
    elif user_input_integer == 4:
        for problem in paths:
            graph = readprob(problem)
            solution = color_dsatur(graph)
            periods, feasible = evaluate(graph, solution)

            if feasible == True:
                better_solution(problem, solution, periods)
                print(f"solution uses {periods} periods")
            else:
                print("not feasible")
