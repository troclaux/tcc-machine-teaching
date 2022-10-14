import pickle
import os
from tqdm import tqdm

with open('solutions.pkl', 'rb') as f:
    
    data = pickle.load(f)
    directory = os.getcwd()

    for i, enunciado in enumerate(tqdm(data)):
        j = 0
        problem_id = str(enunciado["problem_id"])
        solution_id = "solution_" + str(i)
        solution_id_path = "solution_" + str(i) + ".py"
        # solution_txt = str(i) + ".txt"
        path = os.path.join(directory, "problems")
        path = os.path.join(path, problem_id)
        path_id = os.path.join(path, solution_id_path)
        path_stmts = os.path.join(path, "import_stmts.py")
        # path_txt = os.path.join(path, solution_txt)

        if not os.path.exists(path):
            os.makedirs(path)

        with open(path_id, 'w', encoding="utf-8") as g:
            g.write(enunciado["solution"])

        if j == 0:
            with open(path_stmts, 'w', encoding="utf-8") as h:
                h.write("import " + solution_id)
                j += 1
        else:
            with open(path_stmts, 'a', encoding="utf-8") as h:
                h.write("import " + solution_id)
