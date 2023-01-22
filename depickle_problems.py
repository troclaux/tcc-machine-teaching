import pickle
import os
import pandas as pd
import shutil

with open('problems.pkl', 'rb') as f:
    data = pickle.load(f)

    for enunciado in data:
        
        directory = os.getcwd()
        name_id = str(enunciado["id"])
        name_id_txt = name_id + ".txt"
        name_id_csv = name_id + ".csv"

        path_src = os.path.join(directory, "tests")
        path_src_conf = os.path.join(path_src, "conftest.py")
        path_src = os.path.join(path_src, name_id)
        path_src_input = os.path.join(path_src, f"test_input_{name_id}")
        path_src_graph = os.path.join(path_src, f"test_graph_{name_id}")
        path_src_mutation = os.path.join(path_src, f"test_mutation_{name_id}")
        
        path = os.path.join(directory, "problems")
        path = os.path.join(path, name_id)

        path_txt = os.path.join(path, name_id_txt)
        path_df = os.path.join(path, name_id_csv)
        path_conf = os.path.join(path, "conftest.py")
        path_input = os.path.join(path, f"test_input_{name_id}")
        path_graph = os.path.join(path, f"test_graph_{name_id}")
        path_mutation = os.path.join(path, f"test_mutation_{name_id}")

        os.makedirs(os.path.dirname(path_txt), exist_ok=True)

        shutil.copy(path_src_conf, path_conf)
        shutil.copy(path_src_input, path_input)
        shutil.copy(path_src_graph, path_graph)
        shutil.copy(path_src_mutation, path_mutation)

        with open(path_txt, 'a', encoding="utf-8") as g:
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
