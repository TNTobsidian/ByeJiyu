import time,os
c1 = 0
while True:
    timer = int(input('请输入定时关闭极域电子教室的秒数'))
    print('您的秒数是否是'+str(timer)+'?')
    c1 = str(input('输入1代表是，其他皆为否，会重新设置秒数。'))
    if c1 == str('1'):
        print('五秒钟后运行程序。')
        time.sleep(5)
        while timer > 0:
            timer = timer - 1
            print('还有'+str(timer)+'秒关闭极域电子教室！')
            time.sleep(1)
        if timer <= 0:
            print('正在关闭极域电子教室')
            os.system("taskkill /f /im StudentMain.exe /t")
            print('命令已执行')
            break
    else:
        print('goto line 2')
