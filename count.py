import sys
import os
import pandas as pd
from itertools import product
from tqdm import tqdm
#[736, 742, 744, 751, 804, 806, 807, 809, 810, 811, 812, 815, 816, 817, 819, 820, 821, 822, 823, 824, 838, 839, 840, 842]
problem_id = [736, 744, 751, 798, 800, 804, 806, 807, 809, 810, 811, 812, 815, 816, 817, 819, 820, 821, 822, 823, 824, 827, 828, 829, 831, 832, 833, 834, 835, 836, 838, 839, 840]
criteria = ["input", "graph", "mutation"]
problem_count = len(problem_id)

directory = os.getcwd()
path_csv =  os.path.join(directory, "CSV")
path_fig = os.path.join(directory, "Fig")
os.makedirs(path_fig, exist_ok=True)

totals = []
count = 0
for i, problem in enumerate(tqdm(problem_id)):
    path_solution = os.path.join(path_csv, f"solution_{problem}.csv")
    path_test = os.path.join(path_csv, f"test_{problem}.csv")
    df_solution = pd.read_csv(path_solution)
    df_solution["new_outcome"] = df_solution["input_outcome"] & df_solution["graph_outcome"] & df_solution["mutation_outcome"]

    df_test = pd.read_csv(path_test)
    total = len(df_solution)
    PFFF = len(df_solution.query(
            f'old_outcome == 1 & (input_outcome == 0 | graph_outcome == 0 |  mutation_outcome == 0)'
            ))
    PFAA = len(df_solution.query(
            f'old_outcome == 1 & input_outcome == 0'
            ))
    PAFA = len(df_solution.query(
            f'old_outcome == 1 & graph_outcome == 0'
            ))
    PAAF = len(df_solution.query(
            f'old_outcome == 1 & mutation_outcome == 0'
            ))
    FAAA = len(df_solution.query(
            f'old_outcome == 0'
            ))
    AFuFuF = len(df_solution.query(
            f'input_outcome == 0 | graph_outcome == 0 |  mutation_outcome == 0'
            ))
    FPPP = len(df_solution.query(
            f'old_outcome == 0 & input_outcome == 1 & graph_outcome == 1 &  mutation_outcome == 1'
            ))
    totals.append([problem, total, PFFF, PFAA, PAFA, PAAF, FAAA, AFuFuF, FPPP])
    count += PFFF
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0
sum6 = 0
sum7 = 0
sum8 = 0
per_sum = 0
for total in totals:
    
    sum1 += total[1]
    sum2 += total[2]
    sum3 += total[3]
    sum4 += total[4]
    sum5 += total[5]
    sum6 += total[6]
    sum7 += total[7]
    sum8 += total[8]
    per_sum += round(100*total[2]/total[1], 2)
    print(f'''total de soluções para o problema {total[0]}: {total[1]}
    defeitos ineditos entrada: {total[3]}
    defeitos ineditos grafo: {total[4]}
    defeitos ineditos mutação: {total[5]}
    defeitos ineditos total: {total[2]}
    defeitos antigos: {total[6]}
    defeitos novos: {total[7]}
    defeitos não identificados: {total[8]}
    porcentagem entrada: {round(100*total[3]/total[1], 2)}%
    porcentagem grafo: {round(100*total[4]/total[1], 2)}%
    porcentagem mutação: {round(100*total[5]/total[1], 2)}%
    porcentagem total: {round(100*total[2]/total[1], 2)}%
    porcentagem antigos: {round(100*total[6]/total[1], 2)}%
    porcentagem novos: {round(100*total[7]/total[1], 2)}%
    porcentagem não identificados: {round(100*total[8]/total[1], 2)}''')

print(f'''total de soluções: {sum1}
    defeitos ineditos entrada: {sum3}
    defeitos ineditos grafo: {sum4}
    defeitos ineditos mutação: {sum5}
    defeitos ineditos total: {sum2}
    defeitos antigos: {sum6}
    defeitos novos: {sum7}
    defeitos não identificados: {sum8}
    porcentagem entrada: {round(100*sum3/sum1, 2)}%
    porcentagem grafo: {round(100*sum4/sum1, 2)}%
    porcentagem mutação: {round(100*sum5/sum1, 2)}%
    porcentagem total: {round(100*sum2/sum1, 2)}%
    porcentagem antigos: {round(100*sum6/sum1, 2)}%
    porcentagem novos: {round(100*sum7/sum1, 2)}%
    porcentagem não identificados: {round(100*sum8/sum1, 2)}%
    média porcentagem defeitos inéditos: {round(per_sum/problem_count, 2)}%''')