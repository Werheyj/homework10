from threading import Thread
from datetime import datetime
import time


def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


time_start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа потоков {time_res}')

THE_ARGS = ((10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt'))

time_start = datetime.now()

thr_first = Thread(target=write_words, args=THE_ARGS[0])
thr_second = Thread(target=write_words, args=THE_ARGS[1])
thr_third = Thread(target=write_words, args=THE_ARGS[2])
thr_fourth = Thread(target=write_words, args=THE_ARGS[3])

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа потоков {time_res}')
