from collections import Counter
def mean(lst,n):
  get_sum = sum(lst)
  return get_sum/n

def med(lst,n):
  lst.sort()
  if n % 2 == 0:
    median1 = lst[n//2]
    median2 = lst[n//2 - 1]
    median = (median1 + median2)/2
  else:
    median = lst[n//2]
  return median

def mod(lst,n):
  data = Counter(lst)
  get_mode = dict(data)
  mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
  
  if len(mode) == n:
    get_mode = "No mode found"
  else:
    get_mode = "Mode is / are: " + ', '.join(map(str, mode))
      
  return(get_mode)







n_num = [1, 2, 3, 4, 5]
n = len(n_num)
  
print(mean(n_num,n))
print(med(n_num,n))
print(mod(n_num,n))



