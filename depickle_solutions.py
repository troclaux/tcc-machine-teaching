import pickle
import os

with open('solutions.pkl', 'rb') as f:
    
    data = pickle.load(f)
    directory = os.getcwd()

    for i, enunciado in enumerate(data):
        problem_id = str(enunciado["problem_id"])
        solution_id = "solution_" + str(i) + ".py"
        # solution_txt = str(i) + ".txt"
        path = os.path.join(directory, "problems")
        path = os.path.join(path, problem_id)
        path_id = os.path.join(path, solution_id)
        # path_txt = os.path.join(path, solution_txt)

        if not os.path.exists(path):
            os.makedirs(path)

        with open(path_id, 'w', encoding="utf-8") as g:
            g.write(enunciado["solution"])
