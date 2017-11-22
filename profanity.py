import urllib

def read():
    data = open("file.txt")
    content = data.read()
    data.close()
    check_profanity(content)

def check_profanity(text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    output = connection.read()
    # print(output)
    connection.close()
    if "true" in output:
        print("profanity founded")
    elif "false" in output:
        print("Clean words !")
    else:
        print("Scan error ")

read()
