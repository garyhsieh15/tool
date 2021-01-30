
FILE_NAME = "./file/TAP024.txt"
#FILE_NAME = "./file/TCU081.txt"

FILE_NAME_W = "./file/TAP024_W.txt"

"""
open(路徑+檔名,讀寫模式) 
r:讀, w:新建(會覆蓋原有檔案),a追加,b二進位制檔案.

讀寫模式的型別有：
rU 或 Ua 以讀方式開啟, 同時提供通用換行符支援 (PEP 278)
w      以寫方式開啟，
a      以追加模式開啟 (從 EOF 開始, 必要時建立新檔案)

r      以讀模式開啟
w      以寫模式開啟 (參見 w)
a      以寫模式開啟 (參見 a)

rb     以二進位制讀模式開啟
wb     以二進位制寫模式開啟 (參見 w)
ab     以二進位制追加模式開啟 (參見 a)
"""

# -------------------------------------------------------------------------------------
# name       : read_acc_history()
# description: read history of acc data.
#

# date       : 20210126
# author     : garyhsieh
# -------------------------------------------------------------------------------------
def read_acc_history(_fname):

    try:
        ACC_HIS = []
        with open(_fname, 'r') as f:
            ACC_HIS = f.readlines()

    except FileNotFoundError:
        print(">>> couldn't find", "\"" + _fname + "\".")

    except IsADirectoryError:
        print(">>> ", "\"" + _fname + "\"", "is a directory")

    except:
        print(">>> error !!, couldn't read", "\"" + _fname + "\"" + '.')

    else:
        print(">>> find", "\"" + _fname + '".')

    finally:
        print("do no matter what")

    isSearched = False
    time = []
    up_acc = []
    NS_acc = []
    EW_acc = []
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
    """ 
    print("time: ", time)
    print("up: ", up_acc)
    print("NS: ", NS_acc)
    print("EW: ", EW_acc)
    """
    print("f.closed: ", f.closed)

    return time, up_acc, NS_acc, EW_acc

# -------------------------------------------------------------------------------------
# name       : write_acc_history()
# description: write history of acc data.
#
# date       : 20210126
# author     : garyhsieh
# -------------------------------------------------------------------------------------
def write_acc_history(_fname):
    
    text = "89.995     4.299     5.574     0.049\n"

    with open(_fname, 'a') as fw:
        fw.write(text)

if __name__ == "__main__":
    t, up, ns, ew = read_acc_history(FILE_NAME)
    print("show time: ", t)

    #write_acc_history(FILE_NAME_W)

