import xlrd
import qrcode
import os#系统库，判断是本地二维码文件还是网络二维码
import cv
import requests#下载网站二维码
import zbar
from pyzbar.pyzbar import decode #解析二维码的库
import zxing #解析二维码的库

data = xlrd.open_workbook("/Users/jack/PycharmProjects/pythonProject/qr.xlsx")
table = data.sheets()[0]


def pyzbarParseQRCode(filePath):
    if os.path.isfile(filePath):  # 判断是否是本地文件
        img = cv.imread(filePath)  # 读取二维码图片
    else:  # 解析网站验证码
        with open("./qrCodeTest.png", "wb") as f:  # 下载图片保存到本地
            f.write(requests.get(url=filePath).content)
        img = cv.imread("./qrCodeTest.png")  # 读取图片
    texts = decode(img)  # 解码验证码图片
    for text in texts:  # 遍历解码数据
        qrInfo = text.data.decode("utf-8")  # 将内容解码成指定格式
        print(qrInfo)  # 打印
sheet1_nrows = table.nrows
for i in range(sheet1_nrows):  # 逐行打印sheet1数据
    print(table.row_values(i))
    pyzbarParseQRCode(table.row_values(i)[4])
    # print(table.row_values(i)[0])


