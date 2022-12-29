import re
import numpy as np
import pandas as pd

# pattern = re.compile(ur'[0-9]+\.[0-9]+ms')
# #处理文件的正则表达式
# BG = re.compile('[0-9]+\.[0-9]+ms', re.S|re.M)
# Snap = re.compile(r'\[Snapsender\]\sTIMESTAMP\[[0-9]{11}\]\sSIZE\[[0-9]{4,6}\]$', re.S|re.M)
# snap2=re.compile(r'/[api]+/[a-zA-z]+/[a-zA-z0-9]+',re.S|re.M)
#
# # 初始张数为0
# BgNo = 0
# SnapNo = 0

# a[][]
## 1.各个接口请求数排序
## 2.接口的请求时间排序

## 1. hash X 转换的太大
## 2. 对象分配到map，新的往后累加
apiMap = {}

apiList = np.array([[], []])


# 获取api的index
def hashapi(api):
    if api in apiMap:
        return apiMap[api]
    else:
        apiMap[api] = len(apiMap)
    return apiMap[api]


# >>> df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'), index=['x', 'y'])
#         >>> df
#            A  B
#         x  1  2
#         y  3  4
#         >>> df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'), index=['x', 'y'])
#         >>> df.append(df2)
def parse(file):
    find1 = re.compile(r'/[api]+/[a-zA-z]+/[a-zA-z0-9]+', re.S | re.M)
    findTim = re.compile('[0-9]+[.][0-9]+[ms]+', re.S | re.M)
    log = open(file)
    dic = {}
    d2 = {
        'ApiName': pd.Series(['api']),
        'Time': pd.Series(['1.01s']),
    }
    df2 = pd.DataFrame(d2)
    for line in log:
        apiFound = find1.findall(line)
        if apiFound != None and len(apiFound) != 0:
            tim = findTim.findall(line)
            if tim != None and len(tim) != 0:

                print("found api", apiFound, " time:", tim)
                if apiFound[0] in dic:
                    val = dic[apiFound[0]]
                    val = val + 1
                    dic[apiFound[0]] = val
                    print(hashapi(apiFound[0]))
                else:
                    dic[apiFound[0]] = 1
    for index in dic:
        print("api:", index, "num:", dic[index])
    print("apiNum:", len(dic))


def apiappend(index, val):
    np.append(apiList[index], val)


a = np.array([1, 2, 3])
newArray = np.insert(a, 1, 90)
print(a)
print(apiList)
# parse("./run.log")

d2 = {
    'ApiName': pd.Series(['api']),
    'Time': pd.Series(['1.01s']),
}
df2 = pd.DataFrame(d2)
# >>> df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'), index=['x', 'y'])
#         >>> df
#            A  B
#         x  1  2
#         y  3  4
#         >>> df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'), index=['x', 'y'])
#         >>> df.append(df2)
# columns = ['a', 'b', 'c']
pd.DataFrame([[], ])
api=[['api/user/login', '1.01s']]
df3 = pd.DataFrame(api, columns=['ApiName', 'Time'])
print("df3", df3)
df2 = df2.append(df3)
print("df2", df2)
