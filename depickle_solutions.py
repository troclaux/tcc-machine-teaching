import pickle
import os

with open('solutions.pkl', 'rb') as f:

    solucoes_aprovadas = 0
    solucoes_reprovadas = 0
    
    i = 0
    data = pickle.load(f)
    directory = os.getcwd()

    for enunciado in data:
        problem_id = str(enunciado["problem_id"])
        solution_id = "solution_" + str(i) + ".py"
        # solution_txt = str(i) + ".txt"
        path = os.path.join(directory, "problems")
        path = os.path.join(path, problem_id)
        path_id = os.path.join(path, solution_id)
        # path_txt = os.path.join(path, solution_txt)

        if not os.path.exists(path):
            os.makedirs(path)

        # with open(path_txt, 'w', encoding="utf-8") as g:
        #     g.write(enunciado["outcome"])
        with open(path_id, 'w', encoding="utf-8") as g:
            g.write(enunciado["solution"])

        if enunciado["outcome"] == "F":
            solucoes_reprovadas = solucoes_reprovadas + 1
        if enunciado["outcome"] == "P":
            solucoes_aprovadas = solucoes_aprovadas + 1
        i += 1

print(f"solucoes aprovadas: {solucoes_aprovadas}")
print(f"solucoes reprovadas: {solucoes_reprovadas}")
