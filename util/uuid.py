from datetime import datetime
import time


def get_time_uid() -> int:
    return int(time.time() * 1e3)


def get_today_date_string():
    # 获取今天的日期
    today = datetime.today()
    # 将日期对象转换为指定格式的字符串
    date_string = today.strftime('%Y-%m-%d')  # 格式化为 YYYY-MM-DD 的形式
    return date_string
