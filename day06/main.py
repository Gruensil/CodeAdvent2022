import time

n = 4

def check_n_chars(input, idx):
    for ix, charx in enumerate(input[idx:idx+n-1]):
        for iy, chary in enumerate(input[idx+ix+1:idx+n]):
            if charx == chary:
                return False
    return True

def check_input_for_n(input):
    for idx in range(len(input)-n):
        if check_n_chars(input, idx):
            return idx
    return False

with open('C:\\Users\\gruen\\Documents\\CodeAdvent2022\\day06\\input.txt') as f:
    line = f.readline()
    tic = time.perf_counter()
    n = 14
    idx = check_input_for_n(line)
    toc = time.perf_counter()
    print (f"{n} individual chars found at pos {idx}!")
    print (f"Therefor the result is {idx + n}")
    print(f"Found solution in {toc - tic:0.4f} seconds") # 0.0012s

