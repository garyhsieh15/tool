import csv
import pandas as pd
import os

from package import edit_excel_pandas as eep


FILE_NAME = "./file/TAP024.txt"
#FILE_NAME = "./file/TCU081.txt"

FILE_NAME_CSV = "./file/data1.csv"
FILE_NAME_EXCEL = "./file/20210806_Tn.xlsx"

FILE_NAME_W = "./file/TAP024_W.txt"
FILE_NAME_W_CSV = "./file/data1_w.csv"
FILE_NAME_W_TO_CSV = "./file/data2_w.csv"
FILE_NAME_W_TO_EXCEL = "./file/data_w_excel.xlsx"

"""
open(路徑+檔名,讀寫模式, encoding = 'utf8(or utf_8)') 
with open(路徑＋檔名, 操作模式, encoding = 'utf8(or utf_8)') as f:

讀寫模式的型別有：
r      讀取(預設)．
w      寫入(若檔案已存在，先將內容刪除，然後再寫入)．
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
        print(">>> do no matter what")

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

# -------------------------------------------------------------------------------------
# name       : rw_data_csv_01()
# description: read and write csv format'data via pandas module.
#
# date       : 20210807
# author     : garyhsieh
# -------------------------------------------------------------------------------------
def rw_data_csv_01(_fname):
    _data = pd.read_csv(_fname,
            encoding = "utf8",
            header = 0,
            sep = ',',
            skipinitialspace = True,
            #names = ["t", "vel", "hight"],
            #index_col = "vel"
            )

    """
    # show data
    print(">>> show _data:\n%s" %  _data)
    # show type of data
    print(">>> show _data.dtypes:\n%s" % _data.dtypes)
    #print(_data.info())
    # show shape of data
    print(_data.shape)
    # show head(), non para means 5 data
    print(">>> show _data.head(3):\n%s" % _data.head(3))
    # 顯示倒數最後的資料，如果沒有指定則為5筆資料。
    print(">>> show _data.tail(1):\n%s" % _data.tail(1))
    # 顯示time欄位底下的0, 1兩筆資料。
    print(">>> show _data[\"time\"][0:2]:\n%s" % _data["time"][0:2])
    # 顯示time欄位底下的全部資料。
    print(">>> show _data[\"time\"]:\n%s" % _data["time"])
    # 插入新的欄位，並且將該欄位取名"acc", 底下的值為"3.3333"。
    _data.insert(1, column = "acc", value = "3.3333")
    # 刪除有NaN值的該列。
    #_data = _data.dropna()
    # 將有NaN的cell填入9999的值。
    _data = _data.fillna(9999)
    # 重新排列height欄位的底下數值，從小到大排列。
    _data = _data.sort_values("height")
    # 重新排列height欄位的底下數值，從大到小排列。
    _data = _data.sort_values("height", ascending = False)
    """
    
    _data["time"][0] = 119

    print(">>> show _data:\n%s" % _data)
   
    # ---------------------------------------------------------------------------------
    # path_or_buf: file name
    # sep(delimiter): 資料區隔的符號
    # na_rep: 空值要填入的值，可設定為NaN
    # float_format: 浮點數的小數點位數
    # columns: 要儲存的行資料
    # header: 是否保存標頭資料，預設True為保留，False為不保留
    # index: index是否保留，True為保留
    # index_label: 設定index的名稱
    # mode: 寫入的模式，預設'w'
    # encoding: utf_8_sig可以讓中文不產生亂碼
    # ---------------------------------------------------------------------------------
    _data.to_csv(path_or_buf = FILE_NAME_W_TO_CSV, sep = ',', na_rep = "NaN", float_format = "%.4f", \
            columns = ["time", "height"], header = True, index = True, index_label = "idx", \
            mode = 'w', encoding = "utf_8_sig")

    return _data

# -------------------------------------------------------------------------------------
# name       : read_data_excel(_fname)
# description: read EXCEL format'data via pandas module.
#
#              df = pandas.DataFrame(字典或陣列資料)
#              dic   -> df = {key: values,
#                           key: valuse,
#                           ...}
#
#              array -> df = [[key, values],
#                             [key, values],
#                             ...
#                             [key, values]]
#
# date       : 20210808
# author     : garyhsieh
# -------------------------------------------------------------------------------------
def read_data_excel(_fname):

    # ---------------------------------------------------------------------------------
    # parameter
    # file path
    # sheet_name: sheet page, if None means showing all sheet pages.
    # usecols: 指定讀取的column行數, 例如["name_00", "name_01", ... ...]
    #          表示讀column名為name_00, name_01的行內容， "A, B, ...E:H"，表示讀column
    #          index為A, B, ...E到H行內容．
    # 
    # nrows: 指定讀取row的列數, 例如nrows = 2表示0 - 1列內容，nrows = 13表示0 - 12列內容．
    # ---------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------
    # data format
    #
    #     col0  col1  col2  ... ...
    # 0   value value value ... ...
    # 1
    # 2
    # .
    # .
    # .
    # N-1
    # ---------------------------------------------------------------------------------

    data = pd.read_excel(_fname, sheet_name = "Joint Displacements")
    #data = pd.read_excel(_fname, sheet_name = "Joint Displacements", usecols = ["TABLE:  Joint Displacements"])
    #data = pd.read_excel(_fname, sheet_name = "Joint Displacements", usecols = "A, C, E:F", nrows = 2)
    #data = pd.read_excel(_fname, sheet_name = None)
    _df = pd.DataFrame(data)
    #print("show initial df:\n%s" % _df)
    
    # 1.   抓取所有的行標題有哪些．

    # 2.   計算所有行標題的數目．

    # 3.   抓取指定行標題，與指定列裡面的內容．
    # 3-1. 抓取指定列裡面的內容．

    # 4. 修改指定行標題，與指定列裡面的內容．
    """
    _df[columns[0]][1] = "TABLEs"
    a01_m = _df[columns[0]][1]
    print("show a01_m: %s" % a01_m)
    """

    # 5. 抓取列的index值與index的長度．
    """
    a00_idx = _df.index[0]
    a01_idx = _df.index[1]
    print("show a00_idx, a01_idx:%s, %s" % (a00_idx, a01_idx))
    print("show len _df.index:%s" % len(_df.index))
    """

    # 6. 顯示頭尾的資料．
    """
    _df_head = _df.head(2)
    _df_tail = _df.tail(4)
    print("show df.head(2):\n%s" % _df_head)
    print("show df.tail(4):\n%s" % _df_tail)
    """

    # 7. 讀取指定列的資料並且抓取列裡面的cell值．
    """
    row_df_00 = _df[0:3]
    print("show df[0:3]:\n%s" % row_df_00)
    row_df_01 = _df[2:3]
    print("show df[2:3]:\n%s" % row_df_01)

    row_df_01_idx = row_df_01.index[0]
    row_df_01_col = row_df_01.columns
    for col in row_df_01_col:
        print("show row'col: %30s, row'cell: %14s" % (col, row_df_01[col][row_df_01_idx]))
    """

    # 8. continue
    

    print(">>> show _df:\n%s" % _df)

    #print("show data type:\n%s" % type(data))
    #print("show df type:\n%s" % type(df))

    return _df

# -------------------------------------------------------------------------------------
# name       : write_data_excel(_fname, _df)
# description: write EXCEL format'data via pandas module.
#
# date       : 20210808
# author     : garyhsieh
# -------------------------------------------------------------------------------------
def write_data_excel(_fname, _df):

    # ---------------------------------------------------------------------------------
    # mode: 'w'表示重新寫檔案，不接續寫檔案．'a'表示接續寫檔案．
    # ---------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------
    # excel_writer: 檔案路徑．
    # sheet_name: 設定sheet的名稱．
    # na_rep: 設定NaN缺失值．
    # columns[]: 指定要儲存的行資料．
    # index: 設定index是否要顯示，True為顯示，False為不顯示．
    # header: 設定行的標題是否要顯示或是重新給定標題，True為顯示，False為不顯示．["topic name"]重新給定標題．
    # index_label: 設定index的標題．
    # startrow: 從第幾列開始儲存資料．
    # startcol: 從第幾行開始儲存資料．
    # freeze_panes = (a, b): 讓a列與b行在滑鼠滾動中固定．
    # ---------------------------------------------------------------------------------
    with pd.ExcelWriter(_fname, mode = 'w') as writer:
        # 可以在這裡面重複執行df.to_excel()，即可以一次儲存多個sheet page．
        _df.to_excel(excel_writer = writer, sheet_name = "JDisplacements", na_rep = 11, columns = ["R3_idx"], \
        #_df.to_excel(excel_writer = writer, sheet_name = "NEW_JD", na_rep = 11, columns = ["R3_idx"], \
        index = True, header = True, index_label = "garyhsieh", startrow = 0, startcol = 0, float_format = "%.3f", \
        freeze_panes = (1, 1))

# -------------------------------------------------------------------------------------
# name       : append_data_excel(_fname, _df)
# description: append EXCEL format'data via pandas module.
#
# date       : 20210808
# author     : garyhsieh
# -------------------------------------------------------------------------------------
def append_data_excel(_fname, _sheet_name, _df):
    
    # ---------------------------------------------------------------------------------
    # mode: 'w'表示重新寫檔案，不接續寫檔案．'a'表示接續寫檔案．
    # ---------------------------------------------------------------------------------
    with pd.ExcelWriter(_fname, mode = 'a') as writer:
        sheet = writer.book
        if _sheet_name in sheet:
            sheet.remove(sheet[_sheet_name])

        # 可以在這裡面重複執行df.to_excel()，即可以一次儲存多個sheet page．
        _df.to_excel(excel_writer = writer, sheet_name = _sheet_name, na_rep = "garyhsieh", columns = ["R3_idx"], \
                index = True, header = True, index_label = "append", startrow = 1, startcol = 1)

    """
    try:
        with pd.ExcelWriter(_fname, mode = 'a') as writer:
            sheet = writer.book
            sheet.remove(sheet[_sheet_name])
            # 可以在這裡面重複執行df.to_excel()，即可以一次儲存多個sheet page．
            _df.to_excel(excel_writer = writer, sheet_name = _sheet_name, na_rep = "garyhsieh", columns = ["R3_idx"], \
                    index = True, header = True, index_label = "append", startrow = 1, startcol = 1)   

    except Exception as e:
        print(">>> Error message: %s" % e)

    except:
        print(">>> occur unknow Error!!")

    else:
        print(">>> find work sheet")

    finally:
        print(">>> do no matter what!!")
    """

if __name__ == "__main__":
    path = os.getcwd()
    print(">>> show path: %s" % path)
    """
    t, up, ns, ew = read_acc_history(FILE_NAME)
    print("show time: ", t)
    write_acc_history(FILE_NAME_W)
    """

    #time, v, h = read_data_csv_00(FILE_NAME_CSV)
    #write_data_csv_00(FILE_NAME_W_CSV)
    #time, v, h = read_data_csv_00(FILE_NAME_W_CSV)


    #rw_data_csv_01(FILE_NAME_CSV)
    df = read_data_excel(FILE_NAME_EXCEL)
    
    df_PP = eep.ExcelPandasOP(df)
    # 1. 抓取所有的行標題有哪些．
    #df_PP.get_col_header()

    # 2. 計算所有行標題的數目．
    #df_PP.get_col_nums()
    
    # 3. 抓取指定行標題，與指定列裡面的內容．
    #df_PP.get_col_row_data(0, 1)

    # 3-1. 抓取某一列的值
    #df_PP.get_row_data(0)

    # 4. 修改指定行標題之指定列裡面的內容．
    df_PP.modify_col_row_data(0, 1, "ggg")

    #write_data_excel(FILE_NAME_W_TO_EXCEL, df)
    #append_data_excel(FILE_NAME_W_TO_EXCEL, "NEW_SHEET", df)
