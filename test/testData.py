#coding: gb2312
#基础类(smBase)的测试代码
import os
import sm.smData as sm

'''
#测试UDB数据源
fileName = r'C:\test\test.udb'

uds = sm.uds(fileName, 'uds')
uds.Create()
uds.CreateRaster('HeBeiRaster', 'Image', 'encLZW', 'IPF_RGB', 512, 114.249, 39.8751, 118.75, 39.833, 0.0000055555555555555558, 0.0000055555555555555558)
uds.AppendRasterFile('HeBeiRaster', 'fileTIF', 'C:\\work\\项目\\华夏明科\\orig\\J50G004005.tif')
uds.AppendRasterFile('HeBeiRaster', 'fileTIF', 'C:\\work\\项目\\华夏明科\\orig\\J50G004076.tif')
uds.Close()
'''
info = sm.GetImgFileInfo('C:\\work\\项目\\华夏明科\\orig\\J50G004005.tif')

print info.fileName
print info.bounds
print info.width
print info.height





