import pyqrcode
import pandas as pd
import time
import multiprocessing
import threading

start = time.perf_counter()


def make_code(title, actual_text):
    name_ = title
    name_ += ".png"
    qr_code = pyqrcode.create(actual_text)
    qr_code.png(name_, scale=6)
    print(f"created qr for {title}")


def return_csv_as_dict():
    dict_from_csv = pd.read_csv('file.csv', header=None, index_col=0).squeeze("columns").to_dict()
    return dict_from_csv


if __name__ == "__main__":
    dict_of_items = return_csv_as_dict()

    # --------------------------------------------------------------------------------

    # SYNCHRONOUSLY

    # for key,value in dict_of_items.items():
    #     make_code(key,value)
    #
    # finish = time.perf_counter()
    # print(f' SYNCHRONOUSLY: finished in {round(finish - start, 2)} second(s)')

    # --------------------------------------------------------------------------------

    # MULTIPROCESSING

    # processes = []
    # for key, value in dict_of_items.items():
    #     p = multiprocessing.Process(target=make_code, args=(key, value,))
    #     p.start()
    #     processes.append(p)
    #
    # for process in processes:
    #     process.join()
    #
    # finish = time.perf_counter()
    # print(f' MULTIPROCESSING: finished in {round(finish - start, 2)} second(s)')

    # --------------------------------------------------------------------------------

    # THREADING

    threads = []
    for key, value in dict_of_items.items():
        t = threading.Thread(target=make_code, args=(key, value,))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    finish = time.perf_counter()
    print(f' THREADING: finished in {round(finish - start, 2)} second(s)')

    # --------------------------------------------------------------------------------
