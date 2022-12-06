import time

def check_four_chars(input, idx):
    for ix, charx in enumerate(input[idx:idx+3]):
        for iy, chary in enumerate(input[idx+ix+1:idx+4]):
            if charx == chary:
                return False
    return True

def check_input(input):
    for idx in range(len(input)-4):
        if check_four_chars(input, idx):
            return idx
    return False

with open('C:\\Users\\gruen\\Documents\\CodeAdvent2022\\day06\\input.txt') as f:
    line = f.readline()
    tic = time.perf_counter()
    idx = check_input(line)
    toc = time.perf_counter()
    print (f"4 individual chars found at pos {idx}!")
    print (f"Therefor the result is {idx + 4}")
    print(f"Found solution in {toc - tic:0.4f} seconds") # 0.0012s

