import numpy as np
numbers=np.array([9,1,5,3,3,3,2,9,0])
def calculation(numbers):
    length=numbers.size
    if length> 9:
        raise ValueError("List must contain nine numbers")
    else:
        results=numbers.reshape(3,3)
        
        "mean"
        column_mean,row_mean,whole_mean=np.mean(results,axis=0),np.mean(results,axis=1),np.mean(results)
        "variance"
        column_var,row_var,whole_var=np.var(results,axis=0),np.var(results,axis=1),np.var(results)
        "standard deviation"
        column_std,row_std,whole_std=np.std(results,axis=0),np.std(results,axis=1),np.std(results)
        "max"
        column_max,row_max,whole_max=np.max(results,axis=0),np.max(results,axis=1),np.max(results)
        "min"
        column_min,row_min,whole_min=np.min(results,axis=0),np.min(results,axis=1),np.min(results)
        "sum"
        column_sum,row_sum,whole_sum=np.sum(results,axis=0),np.sum(results,axis=1),np.sum(results)



        "the dictionary"
        out={
            "mean":[column_mean.tolist(),row_mean.tolist(),whole_mean.tolist()],
            "variance":[column_var.tolist(),row_var.tolist(),whole_var.tolist()],
            "standard deviation":[ column_std.tolist(),row_std.tolist(),whole_std.tolist()],
            "max":[column_max.tolist(),row_max.tolist(),whole_max.tolist()],
            "min":[column_min.tolist(),row_min.tolist(),whole_min.tolist()],
            "sum":[column_sum.tolist(),row_sum.tolist(),whole_sum.tolist()]}

    return out

final=calculation(numbers)
for key,value in final.items():
    print(f"{key}:{value}")
