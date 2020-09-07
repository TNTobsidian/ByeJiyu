import time
import os
def timeshut():
    print('最终的10秒钟~')
    os.system('shutdown -s -t 10')
    time.sleep(9)
    print('Bye~!')
choose = str(input('请选择执行内容。\n1为清理极域电子教室\n2为打开极域电子教室\n3为定时关机\n4为当场关机\n5为删掉极域电子教室\n谨慎操作！\n您的选择是：'))
print('正在判断选项')
if choose == str('1'):
    print('您的选择为 结束极域电子教室')
    os.system("taskkill /f /im StudentMain.exe /t")
    print('Success!~恭喜你摆脱了老师的监控！')
elif choose == str('2'):
    print('您的选择为 重新打开极域电子教室')
    print('您需要手动关闭本窗口！')
    print('您又进入了老师的监控！~享受吧~！')
    os.system("ReopenStudentMain.bat")
elif choose == str('3'):
    print('您的选择为 定时关机！')
    sleeptime = int(input('请输入您想要定时关机的秒数：'))
    print('正在倒计时...')
    while sleeptime > 0:
        sleeptime = sleeptime -1
        print('还有'+str(sleeptime)+'秒关机！')
        time.sleep(1)
    print('最后十秒钟！')
    timeshut()
elif choose == str('4'):
    print('怎么可能当场嘛~ 给你延长十秒钟嘛')
    os
