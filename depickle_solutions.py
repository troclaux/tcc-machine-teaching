import pickle
import os

with open('solutions.pkl', 'rb') as f:
    data = pickle.load(f)
    i = 0
    for enunciado in data:
        directory = os.getcwd()
        problem_id = str(enunciado["problem_id"])
        solution_id = str(i) + ".py"
        solution_txt = str(i) + ".txt"
        path = os.path.join(directory, "problems")
        path = os.path.join(path, problem_id)
        path_id = os.path.join(path, solution_id)
        path_txt = os.path.join(path, solution_txt)
        with open(path_id, 'w', encoding="utf-8") as g:
            g.write(enunciado["solution"])
        with open(path_txt, 'w', encoding="utf-8") as g:
            g.write(enunciado["outcome"])
        i += 1