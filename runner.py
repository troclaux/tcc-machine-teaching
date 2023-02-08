from save_tests_output_main import save_tests_output
from itertools import product
from joblib import Parallel, delayed
import time

#problem_id = [736, 742, 744, 751, 804, 806, 807, 809, 810, 811, 812, 815, 816, 817, 819, 820, 821, 822, 823, 824, 838, 839, 840, 842]
#criteria = ["input", "graph", "mutation"]
problem_id = [736, 742, 744, 751, 804, 806, 807, 809, 810, 811, 812, 815]
#problem_id = [816, 817, 819, 820, 821, 822, 823, 824, 838, 839, 840, 842]
#criteria = ["input"]
criteria = ["graph"]
#criteria = ["mutation"]
executions = []
for args in product(criteria, problem_id):
    list = [args[0],args[1]]
    executions.append(list)

start = time.time()
Parallel(n_jobs=12, verbose=5)(delayed(save_tests_output)(i[0],i[1]) for i in executions)
end = time.time()
print('{:.4f} s'.format(end-start))
