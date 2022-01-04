import pyautogui
import random

pyautogui.locateAllOnScreen()

loading_img = './auto_img/aknights/loading.png'
action_blue_img = './auto_img/aknights/action_blue.png'
action_red_img = './auto_img/aknights/action_red.png'
activity_img = './auto_img/aknights/activity.png'
complete_img = './auto_img/aknights/complete.png'
san_yes_img = './auto_img/aknights/san_yes.png'
yuanshi_img = './auto_img/aknights/yuanshi.png'
terminal_img = './auto_img/aknights/terminal.png'
yikaiqi_img = './auto_img/aknights/yikaiqi.png'

def click_img(img):
    pyautogui.sleep(1)
    location = pyautogui.locateOnScreen(image=img)
    # 输出坐标
    # print(location)
    # 利用center()函数获取目标图像在系统中的中心坐标位置
    if location:
        x, y = pyautogui.center(location)
        # print('center()', x, y)
        pyautogui.click(x=x, y=y, clicks=1, button='left')
        return True, location
    return False, None

def end_or_not(img,times):
    pyautogui.sleep(1)
    location = pyautogui.locateOnScreen(image=img)
    if location:
        if times > 0:
            x, y = pyautogui.center(location)
            pyautogui.click(x=x, y=y, clicks=1, button='left')
            print(f"已补充体力，还需补充体力次数：{times-1}")
            return True, times-1
        return False, None
    return False, -999

def test(img):
    location = pyautogui.locateOnScreen(image=img)
    # 输出坐标
    print(location)

def load():
    click_img(loading_img)

def start_activity(cost_time, add_times):
    count = 0
    add_times_need =add_times
    fail_times = 0
    while add_times_need>=0:
        pyautogui.sleep(1)
        # 点击开始行动
        flag_1,pos_1 = click_img(action_blue_img)
        if flag_1:
            pos_true = pos_1
        print(f"开始行动：{flag_1},当前失败次数：{fail_times}")
        if pyautogui.locateOnScreen(image=yuanshi_img):
            return False
        flag_3, add_times_renew = end_or_not(san_yes_img,add_times_need)
        if flag_3 is False and add_times_renew is None:
            print(f"已执行结束，执行次数：{count}；补充体力次数：{add_times}")
            return True
        if flag_3:
            pyautogui.sleep(2)
            add_times_need = add_times_renew
            click_img(action_blue_img)
        flag_2, pos_2 = click_img(action_red_img)
        if flag_2:
            pos_true_red = pos_2		
            count = count + 1
            fail_times = 0
            print(f"正在执行第{count}次")

        if not flag_2:
            fail_times = fail_times + 1
            if fail_times > 3:
				# 待修改，额外物资误触
                x, y = pyautogui.center(pos_true)
                pyautogui.click(x=x, y=y, clicks=1, button='left')
            if fail_times > 8:
                a,b = pyautogui.center(pos_true_red)
                pyautogui.click(x=2*a-x, y=2*b-y, clicks=1, button='left')
                fail_times = fail_times-5 
            continue
        pyautogui.sleep(cost_time)
        print(f"计时{cost_time}秒结束")

        print(f"已开启 ：{click_img(yikaiqi_img)[0]}")
        x, y = pyautogui.center(pos_true)
        pyautogui.click(x=x, y=y, clicks=1, button='left')
        print(f"complete ")
        pyautogui.sleep(2)
    return True

if __name__ == '__main__':
    # load()
    # start_activity(185,0)
    print("1-7执行时间为75秒")
    x = input ("输入执行任务时间、需要补充体力次数:")
    a,b = map(int,x.split())
    start_activity(a,b)
	
    # start_activity(75,0)
