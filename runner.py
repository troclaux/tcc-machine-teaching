from save_tests_output_main import save_tests_output
from itertools import product
from joblib import Parallel, delayed
import time

#problem_ids = [736, 742, 744, 751, 798, 800, 804, 806, 807, 809, 810, 811, 812, 815, 816, 817, 819, 820, 821, 822, 823, 824, 827, 828, 829, 831, 832, 833, 834, 835, 836, 838, 839, 840, 842]
#criteria = ["input", "graph", "mutation"]
#problem_ids = [736, 742, 744, 751, 798, 800, 804, 806, 807, 809, 810, 811]
#problem_ids = [812, 815, 816, 817, 819, 820, 821, 822, 823, 824, 827, 828]
#problem_ids = [829, 831, 832, 833, 834, 835, 836, 838, 839, 840, 842]
problem_ids = [809]
#problem_ids = [817, 819, 822, 823, 828, 832, 834, 838]
#problem_ids = [829]
criteria = ["input"]
#criteria = ["graph"]
#criteria = ["mutation"]
executions = []
for args in product(criteria, problem_ids):
    permutation = [args[0],args[1]]
    executions.append(permutation)

start = time.time()
Parallel(n_jobs=12, verbose=12)(delayed(save_tests_output)(i[0],i[1]) for i in executions)
end = time.time()
print('{:.4f} s'.format(end-start))
