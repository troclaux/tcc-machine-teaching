import sys
import os
import pandas as pd
from itertools import product
from tqdm import tqdm
import matplotlib.pyplot as plt
import seaborn as sns
#import sqlalchemy as db
#from sqlalchemy.orm import sessionmaker

problem_id = [736, 742, 744, 751, 804, 806, 807, 809, 810, 811, 812, 815, 816, 817, 819, 820, 821, 822, 823, 824, 838, 839, 840, 842]
criteria = ["input", "graph", "mutation"]
'''
url_object = db.URL.create(
    "mysql+pymysql",
    username="root",
    password="RootSenha",  # plain (unescaped) text
    host="127.0.0.1",
    database="tcc_machine_teaching",
)
engine = db.create_engine(url_object)
#engine = db.create_engine("mysql://root:RootSenha@127.0.0.1/tcc_machine_teaching")

Session = sessionmaker(engine)
'''
directory = os.getcwd()
path_csv =  os.path.join(directory, "CSV")
path_fig = os.path.join(directory, "Fig")
os.makedirs(path_fig, exist_ok=True)

executions = []
for args in product(criteria, problem_id):
    permutation = [args[0],args[1]]
    executions.append(permutation)
#criteria,id

for i, problem in enumerate(tqdm(problem_id)):
    path_solution = os.path.join(path_csv, f"solution_{problem}.csv")
    path_test = os.path.join(path_csv, f"test_{problem}.csv")
    df_solution = pd.read_csv(path_solution)
    df_test = pd.read_csv(path_test)
    df_heatmap = pd.DataFrame(0, index=["F", "P"], columns=["FFF", "FFP", "FPF", "PFF", "FPP", "PFP", "PPF", "PPP"])
    positions = product(["F", "P"], ["FFF", "FFP", "FPF", "PFF", "FPP", "PFP", "PPF", "PPP"])
    size = len(df_solution)
    for position in positions:
        foo = foo if 'foo' in locals() else 'default'
        old = 0 if position[0] == "F" else 1
        input = 0 if position[1][0] == "F" else 1
        graph = 0 if position[1][1] == "F" else 1
        mutation = 0 if position[1][2] == "F" else 1
        count = len(df_solution.query(
            f'old_outcome == {old} & input_outcome == {input} & graph_outcome == {graph} & mutation_outcome == {mutation}'
            ))
        df_heatmap[position[1]][position[0]] = count/size
    fig, ax = plt.subplots(figsize=(10,10)) 
    heatmap = sns.heatmap(df_heatmap, annot=True, fmt='.2%', cmap='Blues', square=True)
    heatmap_path = os.path.join(path_fig, f"heatmap_{problem}.png")
    heatmap.figure.savefig(heatmap_path)
    plt.close()
    #for criterion in criteria:
        
		

#save_tests_output("input",820)