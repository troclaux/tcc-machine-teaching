import pickle
import os
import pandas as pd
import shutil

problem_ids = [736, 742, 744, 751, 804, 806, 807, 809, 810, 811, 812, 815, 816, 817, 819, 820, 821, 822, 823, 824, 838, 839, 840, 842]
criteria = ["input", "graph", "mutation"]
directory = os.getcwd()
path_csv =  os.path.join(directory, "CSV")
os.makedirs(path_csv, exist_ok=True)
for problem_id in problem_ids:
    path_csv_solution =  os.path.join(path_csv, f"solution_{problem_id}.csv")
    values_solution = pd.DataFrame({'solution_id': pd.Series(dtype='int'),
                                    'problem_id': pd.Series(dtype='int'),
                                    'old_outcome': pd.Series(dtype='bool_'),
                                    'input_outcome': pd.Series(dtype='bool_'),
                                    'graph_outcome': pd.Series(dtype='bool_'),
                                    'mutation_outcome': pd.Series(dtype='bool_'),
                                    'input_result': pd.Series(dtype='str'),
                                    'graph_result': pd.Series(dtype='str'),
                                    'mutation_result': pd.Series(dtype='str')})
            
    #os.makedirs(os.path.dirname(path_csv_solution), exist_ok=True)
    values_solution.to_csv(path_csv_solution, index=False)

    values_test = pd.DataFrame({'test_id': pd.Series(dtype='int'),
                                'problem_id': pd.Series(dtype='int'),
                                'criteria_type': pd.Series(dtype='str'),
                                'pass_count': pd.Series(dtype='int'),
                                'fail_count': pd.Series(dtype='int'),
                                'error_count': pd.Series(dtype='int')})
    path_csv_test = os.path.join(path_csv, f"test_{problem_id}.csv")
    #os.makedirs(os.path.dirname(path_csv_test), exist_ok=True)
    values_test.to_csv(path_or_buf=path_csv_test, index=False)

with open('problems.pkl', 'rb') as f:
    data = pickle.load(f)

    for enunciado in data:
        
        directory = os.getcwd()
        name_id = str(enunciado["id"])
        name_id_txt = name_id + ".txt"

        path_csv =  os.path.join(directory, "CSV")
        path_src = os.path.join(directory, "tests")
        path_src_conf = os.path.join(path_src, "conftest.py")
        path_src = os.path.join(path_src, name_id)
        path_src_input = os.path.join(path_src, f"test_input_{name_id}.py")
        path_src_graph = os.path.join(path_src, f"test_graph_{name_id}.py")
        path_src_mutation = os.path.join(path_src, f"test_mutation_{name_id}.py")
        
        path = os.path.join(directory, "problems")
        path = os.path.join(path, name_id)

        path_txt = os.path.join(path, name_id_txt)
        path_conf = os.path.join(path, "conftest.py")
        path_input = os.path.join(path, f"test_input_{name_id}.py")
        path_graph = os.path.join(path, f"test_graph_{name_id}.py")
        path_mutation = os.path.join(path, f"test_mutation_{name_id}.py")

        os.makedirs(os.path.dirname(path_txt), exist_ok=True)

        shutil.copy(path_src_conf, path_conf)
        shutil.copy(path_src_input, path_input)
        shutil.copy(path_src_graph, path_graph)
        shutil.copy(path_src_mutation, path_mutation)

        with open(path_txt, 'w', encoding="utf-8") as g:
            g.write("chapter__label:")
            g.write('\n')
            g.write(enunciado["chapter__label"])
            g.write('\n')
            g.write("id:")
            g.write('\n')
            g.write(str(enunciado["id"]))
            g.write('\n')
            g.write("content:")
            g.write('\n')
            g.write(enunciado["content"])
            g.write('\n')
            g.write('\n')
