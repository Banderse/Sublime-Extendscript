# -*- coding: utf-8 -*-

import sys
from win32com.client import Dispatch

def main(f):
    app = Dispatch('Illustrator.Application.CS5')
    result = app.DoJavaScriptFile(f) # 执行并返回结果
    print(result) # 输出结果至console

if __name__ == '__main__':
    main(sys.argv[1])