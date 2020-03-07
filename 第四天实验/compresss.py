
import optparse
import os
import re
import zipfile


def findFile(path, postfix = 'jpg', move_to=None):
    os.chdir(path)
    ListFile = os.listdir('.')
    print(path)
    List=[]
    for filename in ListFile:
        fileRegex = re.match(r'.*?\.' + postfix, filename)
        if fileRegex:
            List.append(filename)
    if os.path.exists(move_to) and List:
        newZip=zipfile.ZipFile(move_to+'new.zip','w')
        for x in range(len(List)):
           newZip.write(List[x],compress_type=zipfile.ZIP_DEFLATED)
    else:
        return '文件路径不存在'
    return  List


def main():
    parser = optparse.OptionParser("usage%prog " + "-f <type>")
    parser.add_option("-f", dest="type", type="string", help="stype of file file")
    (options, args) = parser.parse_args()
    type = options.type
    print("含有的指定文件有：", findFile('D:\大四\大四下\网络攻防\王教员',str(type),move_to='D:\大四\大四下\网络攻防\于晗\第二天\zip'))


if __name__ == "__main__":
    main()