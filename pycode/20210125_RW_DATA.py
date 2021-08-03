import csv

FILE_NAME = "./file/TAP024.txt"
#FILE_NAME = "./file/TCU081.txt"

FILE_NAME_CSV = "./file/data1.csv"

FILE_NAME_W = "./file/TAP024_W.txt"
FILE_NAME_W_CSV = "./file/data1_w.csv"

"""
open(路徑+檔名,讀寫模式, encoding = 'utf8(or utf_8)') 
with open(路徑＋檔名, 操作模式, encoding = 'utf8(or utf_8)') as f:

讀寫模式的型別有：
r      讀取(預設)．
w      寫入(若檔案已存在，先將內容刪除，然後在寫入)．
a      寫入(若檔案已存在，從最後方追加)．
x      寫入(若該檔案已存在，送出例外FileExistsError通知)．
+      讀取與寫入(檔案同時操作讀取與寫入)．

t      文字模式(預設，很少使用)．
    tr     以文字模式讀取．
    wr     以文字模式寫入．

b      二進位模式．
    rb     以二進位讀模式開啟
    wb     以二進位寫模式開啟 (參見 w)
    ab     以二進位追加模式開啟 (參見 a)
"""

# -------------------------------------------------------------------------------------
# name       : read_acc_history()
# description: read history of acc data, the file formate is txt.
#

# date       : 20210126
# author     : garyhsieh
# -------------------------------------------------------------------------------------
def read_acc_history(_fname):

    try:
        ACC_HIS = []
        with open(_fname, 'r', encoding = "utf8") as f:
            ACC_HIS = f.readlines()
            #ACC_HIS = f.read()

    except FileNotFoundError:
        print(">>> couldn't find file !!", "\"" + _fname + "\".")

    except IsADirectoryError:
        print(">>> ", "\"" + _fname + "\"", "is a directory")

    except:
        print(">>> error !!, couldn't read", "\"" + _fname + "\"" + '.')

    else:
        print(">>> find file", "\"" + _fname + '".')

    finally:
        print("do no matter what")

    isSearched = False
    time = []
    up_acc = []
    NS_acc = []
    EW_acc = []
    print("show all data: ", ACC_HIS)
    for line in ACC_HIS:
        line_list = line.split()
        #print("show line list: ", line_list) 
        if isSearched  == False:
            for cell in line_list:
                #print("show cell:", cell)
                if cell == "#Data:" and isSearched == False:
                    isSearched = True
                    break
            continue

        if isSearched == True:
            if line_list == []:
                break
            #print("length line_list: ", len(line_list))
            time.append(line_list[0])
            up_acc.append(line_list[1])
            NS_acc.append(line_list[2])
            EW_acc.append(line_list[3])

    print("f.closed: ", f.closed)

    return time, up_acc, NS_acc, EW_acc

# -------------------------------------------------------------------------------------
# name       : write_acc_history()
# description: write history of acc data, the file formate is txt.
#
# date       : 20210126
# author     : garyhsieh
# -------------------------------------------------------------------------------------
def write_acc_history(_fname):
    
    text = "89.995     4.299     5.574     0.049\n"

    with open(_fname, 'a', encoding = "utf8") as fw:
        fw.write(text)

# -------------------------------------------------------------------------------------
# name       : read_data_csv_00()
# description: read csv format'data via csv module.
#
# date       : 20210803
# author     : garyhsieh
# -------------------------------------------------------------------------------------
def read_data_csv_00(_fname):
    try:
        DATA1 = []
        with open(_fname, 'r', encoding = "utf8") as fr:
            for k in csv.reader(fr):
                DATA1.append(k)
                #DATA1.extend(k)

    except FileNotFoundError:
        print(">>> couldn't find file !!", "\"" + _fname + "\".")

    except IsADirectoryError:
        print(">>> ", "\"" + _fname + "\"", "is a directory")

    except:
        print(">>> error !!, couldn't read", "\"" + _fname + "\"" + '.')

    else:
        print(">>> find file, path:", "\"" + _fname + '".')

    finally:
        print("do no matter what")

    _time = []
    _v = []
    _h = []

    t_idx = 0
    v_idx = 1
    h_idx = 2
    for line in DATA1:
        #print("show line value: ", line)
        if line[t_idx] == "time":
            continue

        _time.append(line[t_idx])
        _v.append(line[v_idx])
        _h.append(line[h_idx])

    print("show time: ", _time)
    print("show v: ", _v)
    print("show h: ", _h)

    return _time, _v, _h

# -------------------------------------------------------------------------------------
# name       : write_data_csv_00()
# description: write csv format'data via csv module.
#
# date       : 20210804
# author     : garyhsieh
# -------------------------------------------------------------------------------------
def write_data_csv_00(_fname):

    DATA1_W = []
    DATA1_W.append(["time", "v", "h"])
    DATA1_W.append(["0", "2", "4"])
    DATA1_W.append(["0.5", "3.111", "6.123"])
    DATA1_W.append(["1.0", "3.878", "9.432"])

    try:
        with open(_fname, 'w', newline = '', encoding = "utf8") as fw:
            write_data = csv.writer(fw)
            write_data.writerows(DATA1_W)

    except FileNotFoundError:
        print(">>> couldn't find file !!", "\"" + _fname + "\".")

    except IsADirectoryError:
        print(">>> ", "\"" + _fname + "\"", "is a directory")

    except:
        print(">>> error !!, couldn't write", "\"" + _fname + "\"" + '.')

    else:
        print(">>> file exist, path:", "\"" + _fname + '".')

    finally:
        print("do no matter what")

    print("show fw: ", fw)
    print("show DATA1_W: ", DATA1_W)


if __name__ == "__main__":
    """
    t, up, ns, ew = read_acc_history(FILE_NAME)
    print("show time: ", t)
    """

    #time, v, h = read_data_csv_00(FILE_NAME_CSV)
    write_data_csv_00(FILE_NAME_W_CSV)
    time, v, h = read_data_csv_00(FILE_NAME_W_CSV)

    #write_acc_history(FILE_NAME_W)

