import time
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            content = file.readline()
            if content == '':
                break
            all_data.append(content)


files = [f'./file {number}.txt' for number in range(1, 5)]

start = time.time()

for f in files:
    read_info(f)

end = time.time()
print(end-start, '(линейный)')

if __name__ == '__main__':
    start = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files)

    end = time.time()
    print(end-start, '(многопроцессорный)')
