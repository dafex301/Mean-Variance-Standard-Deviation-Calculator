import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        npList = np.array(list).reshape(3,3)

        new_dict = {
            'mean': [npList.mean(axis=0).tolist(), npList.mean(axis=1).tolist(), npList.flatten().mean()],
            'variance': [npList.var(axis=0).tolist(), npList.var(axis=1).tolist(), npList.flatten().var()],
            'standard deviation': [npList.std(axis=0).tolist(), npList.std(axis=1).tolist(), npList.flatten().std()],
            'max': [npList.max(axis=0).tolist(), npList.max(axis=1).tolist(), npList.flatten().max()],
            'min': [npList.min(axis=0).tolist(), npList.min(axis=1).tolist(), npList.flatten().min()],
            'sum': [npList.sum(axis=0).tolist(), npList.sum(axis=1).tolist(), npList.flatten().sum()]
        }

    return new_dict

print(calculate([0,1,2,3,4,5,6,7,8]))