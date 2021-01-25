
import re

cc_list = """gary hsieh <garyhsieh15@gmail.com>,
hsieh hsiao-yung <garyhsieh.twn@gmail.com>,
tom cruise <tomcruise@gmail.com>"""

# -------------------------------------------------------------------------------------
# name       : find_name()
# description: set first name then search the email.
#
# date       : 20210125
# author     : garyhsieh
# -------------------------------------------------------------------------------------
def find_name(name):
    result = ""
    # 事先編譯來增進效能
    regex = re.compile(name + r"([a-zA-Z0-9.]+)\@([a-z]+)\.([a-z]+)")
    result = regex.search(cc_list)
    #result = re.search(name + r"[a-zA-Z0-9.]+@[a-z]+\.[a-z]+", cc_list)
    if result:
        print("found result:", result)
        print("result.group(0): ", result.group(0))
        print("result.group(1): ", result.group(1))
        print("result.group(2): ", result.group(2))

# -------------------------------------------------------------------------------------
# name       : find_all_name()
# description: find all email's names
#
# date       : 20210125
# author     : garyhsieh
# -------------------------------------------------------------------------------------
def find_all_name(_cc_list):
    matched = re.findall(r'([a-zA-Z0-9.]+)\@(\w+)\.(\w+)', _cc_list)
    names = [x[0] for x in matched]
    print(names)


if __name__ == "__main__":
    #print("show all info: ", cc_list)
    #name = "gary"
    name = "tom"
    #name = "cruise"
    find_name(name)
    #find_all_name(cc_list)
