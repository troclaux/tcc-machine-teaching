import pickle
from tqdm import tqdm
import os
from tqdm import tqdm

def create_import_stmts():
    path = os.path.join(directory, "problems")
    #os.system(f"cd {path}")
    for problem in sorted(os.listdir(path)):
        path_problem = os.path.join(path, problem)
        path_stmts = os.path.join(path_problem, "import_stmts.py")
        os.system(f"> {path_stmts}")

with open('solutions.pkl', 'rb') as f:
    data = pickle.load(f)
    directory = os.getcwd()

    create_import_stmts()

    for i, enunciado in enumerate(tqdm(data)):
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


        with open(path_stmts, 'a', encoding="utf-8") as h:
            h.write(f"try:\n\timport {solution_id} \nexcept:\n\tprint('{solution_id} IMPORT ERROR')\n")



