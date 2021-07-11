
import timeit

# -------------------------------------------------------------------------------------
# name       : calc_run_time()
# description: calculate function time of run.
#              timeit.timeit(stmt, setup,timer, number)
#                  stamt: statement, 要測試的程式碼或者語句
#                  setup: 執行的環境，在執行 stmt 前的配置語句, EX:"from __main__ import func_name"
#                  timer: 計時器，一般忽略這個引數
#                  number: stmt 執行的次數，預設是1000000，一百萬
#
#              timeit.repeat(stmt, setup, timer, number, repeat)
#                  repeat: 要反覆執行的次數
#
# date       : 20210712
# author     : garyhsieh
# -------------------------------------------------------------------------------------
def calc_func_time():
    a = 0
    for i in range(10):
        a += i
    
    return a


if __name__ == "__main__":
    # 此函式表示在if __name__ == '__main__'的條件下，執行1次calc_func_time()消耗的時間
    t = timeit.timeit("calc_func_time()", "from __main__ import calc_func_time", number = 1)

    # 此函式表示在if __name__ == '__main__'的條件下，執行1次calc_func_time()消耗的時間, 反覆3次的執行.
    t_repeat = timeit.repeat("calc_func_time()", "from __main__ import calc_func_time", number = 1, repeat = 3)

    print("show time:", t)
    print("show time repeat 3:", t_repeat)
    print("show calc func time:", calc_func_time())
