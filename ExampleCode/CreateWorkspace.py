# coding: GB2312
#===================================
#===================================
import os
import sys
sys.path.append(r"E:\Develop\UGO6.1\01_SourceCode\Builds\Win_Solution_vc9\BinD") #将.net组件的路径添加到环境变量
import smu as sm #导入SuperMap模块



if __name__ == '__main__':
	sm.Init()#初始化Python组件环境;

	bResult = sm.CreateWorkspace(r'F:\Temp\2012-08-25\test.sxwu')
	if bResult == 1:
		print '创建工作空间成功.'
	else:
		print "创建工作空间失败."
	sm.Exit()#清空组件环境释放内存
