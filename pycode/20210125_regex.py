
import re

cc_list = """gary hsieh <garyhsieh15@gmail.com>,
hsieh hsiao-yung <garyhsieh.twn@gmail.com>,
tom cruise <tomcruise@gmail.com>"""

# set first name then search the email.
def find_name(name):
    result = ""
    result = re.search(name + r"[a-zA-Z0-9.]+@[a-z]+\.[a-z]+", cc_list)
    if result:
        print("found result:", result)

if __name__ == "__main__":
    #print("show all info: ", cc_list)
    #name = "gary"
    name = "tom"
    #name = "cruise"
    find_name(name)
