import pickle
import os
import pandas as pd

with open('problems.pkl', 'rb') as f:
    data = pickle.load(f)

    for enunciado in data:
        
        directory = os.getcwd()
        name_id = str(enunciado["id"])
        name_id_txt = name_id + ".txt"
        name_id_csv = name_id + ".csv"
        path = os.path.join(directory, "problems")
        path = os.path.join(path, name_id)
        path_txt = os.path.join(path, name_id_txt)
        path_df = os.path.join(path, name_id_csv)
        #path_tests = os.path.join(path, "tests/")
        path_solutions = os.path.join(path, "solutions/")

        os.makedirs(os.path.dirname(path_txt), exist_ok=True)
        DataFrame = pd.DataFrame(columns=["ID", "Total_tests", "Passed_tests", "Original_outcome"])
        DataFrame.to_csv(path_or_buf = path_df, index=False)

        #if not os.path.exists(path_tests):
        #    os.mkdir(os.path.dirname(path_tests))
        if not os.path.exists(path_solutions):
            os.mkdir(os.path.dirname(path_solutions))
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