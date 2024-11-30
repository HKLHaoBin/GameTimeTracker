import time
import pyperclip

die = 0     # 死亡次数
time_O = 0   # 时间（修改）
win = 0     # 判断是否胜利
time_s = 0
hit = 0

def minutes_to_hours_minutes_seconds(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f"{hours:d}时{remaining_minutes:d}分"

def result():
    try:
        end_time = time.time()
        print("end_time", end_time)
        time_interval = end_time - start_time
        time_m = time_interval / 60
        time_interval = int(time_interval)
        # 计算流逝的时间有多少秒
        time_s = time_interval % 60
        minutes = int(time_m + time_O)
        formatted_time = minutes_to_hours_minutes_seconds(minutes)

        content_to_copy = f"用时"

        if time_m + time_O >= 60:
            content_to_copy += f"{formatted_time}{time_s}秒"
        elif int(time_m + time_O) >= 1 and int(time_m + time_O) < 60:
            content_to_copy += f"{int(time_m + time_O)}分{time_s}秒"
        else:
            content_to_copy += f"{time_s}秒"

        if hit != 0:
            content_to_copy += f",被{hit}次击打,"
        if die != 0:
            content_to_copy += f"失败共{die}次"

        if win == 1:
            content_to_copy += "后胜利!"

        pyperclip.copy(str(content_to_copy))
        print("已复制到剪贴板:", content_to_copy)
    except Exception as e:
        print(f"发生错误: {e}")

    return


# 记录开始时间
start_time = time.time()
print("start_time", start_time)

while True:
    try:
        print(" ")
        useu = input('end t -t +t tt d p now win 回车 ：') # 功能自己研究
        if useu == "":
            hit += 1
            result()
        
        elif useu == "d":
            die += 1
            result()
            hit = 0

        elif useu == "end":
            break

        elif useu == "t":
            useu_t = int(input('改几分钟？：'))
            time_O = useu_t
            result()

        elif useu == "+t":
            useu_t = int(input('加几分钟？：'))
            time_O += useu_t
            result()

        elif useu == "tt":
            useu_tt = int(input('(带重置）改几分钟？：'))
            time_O = useu_tt
            start_time = time.time()
            result()

        elif useu == "dd":
            useu_d = int(input('改死亡次数为？：'))
            die = useu_d
            result()

        elif useu == "p":
            end_time = time.time()
            time_interval = end_time - start_time
            time_m = time_interval / 60
            time_O = time_m + time_O
            time_interval = int(time_interval)
            # 计算流逝的时间有多少秒
            time_s = time_interval % 60
            time_P = input('开始？：')
            if time_P == "":
                # 记录开始时间
                start_time = time.time() - time_s
                print("start_time", start_time)
                result()
            else:
                print("不暂停啊，那我继续了")

        elif useu == "now":
            result()

        elif useu == "win":
            win = 1
            result()
            break

        else:
            print("无效，你误触了吧")
            result()
    except ValueError as ve:
        print(f"无效输入: {ve}")
    except Exception as e:
        print(f"发生错误: {e}")
