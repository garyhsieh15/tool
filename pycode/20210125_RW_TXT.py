
FILE_NAME = "./file/TAP024.txt"
#FILE_NAME = "./file/TCU081.txt"

FILE_NAME_W = "./file/TAP024_W.txt"

# -------------------------------------------------------------------------------------
# name       : read_acc_history()
# description: read history of acc data.
#
# date       : 20210126
# author     : garyhsieh
# -------------------------------------------------------------------------------------
def read_acc_history():

    with open(FILE_NAME, 'r') as f:
        ACC_HIS = f.readlines()

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
def write_acc_history():
    
    text = "89.995     4.299     5.574     0.049\n"

    with open(FILE_NAME_W, 'a') as fw:
        fw.write(text)

if __name__ == "__main__":
    #read_acc_history()
    write_acc_history()

