from datetime import datetime, timedelta
from colorama import Fore, Back, Style

from lib.api import get_daily, get_kfc_v_wo50, get_public_holidays


def get_current_date():
    """
    获取当前日期、星期几、星期几的汉字
    """
    now = datetime.now()
    weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五🤩", "星期六🥳", "星期日🥳"]
    return now.strftime("%Y年%m月%d日"), weekdays[now.weekday()], now.weekday()

def get_days_until(target_date):
    """
    获取距离目标日期还有多少天
    """
    today = datetime.now().date()
    delta = target_date - today
    return delta.days

def get_next_public_holidays():
    """
    获取今年、明年的公共节假日
    """
    # 获取今年
    year = datetime.now().year
    # 获取今年的公共节假日
    this_year = get_public_holidays(year, 'CN')
    # 获取明年的公共节假日
    next_year = get_public_holidays(year + 1, 'CN')
    # 合并两个列表
    holidays = this_year + next_year
    # 获取今天
    today = datetime.now().date()
    # 获取明年的今天日期
    next_year_yesterday = today + timedelta(days=100) # days表示天数以内的假期
    # 保留【今天之后】到【明年昨天之前】的节假日
    holidays = [holiday for holiday in holidays if today <= datetime.strptime(holiday['date'], '%Y-%m-%d').date() < next_year_yesterday]
    return holidays


def get_greeting():
    """
    获取问候语
    """
    current = datetime.now().hour
    if 5 <= current < 12:
        return "上午好"
    elif 12 <= current < 18:
        return "下午好"
    elif 18 <= current < 22:
        return "晚上好"
    else:
        return "夜深了"

def main():
    output = []
    
    current_date, current_weekday, weekdays = get_current_date()
    output.append(f"【摸鱼办】提醒您：\n")
    output.append(f"今天是 {Fore.CYAN}{current_date}{Style.RESET_ALL}，{current_weekday}\n")
    greeting = get_greeting()
    output.append(f"{greeting}！摸鱼人！工作再累，一定不要忘记摸鱼哦！\n有事没事起身去茶水间，去厕所，去廊道走走别老在工位上坐着，钱是老板的，但命是自己的🏃‍♀️‍➡️\n")

    # 计算节日倒计时
    saturday = datetime.now() + timedelta((5 - datetime.now().weekday()) % 7)
    output.append(f"距离【周六】还有：{get_days_until(saturday.date())}天")

    holidays = get_next_public_holidays()
    for holiday in holidays:
        output.append(f"距离【{holiday['localName']}】还有：{get_days_until(datetime.strptime(holiday['date'], '%Y-%m-%d').date())}天")

    daily = get_daily()
    kfc = get_kfc_v_wo50()
    output.append(f"\n{Fore.GREEN}--每日一言--{Style.RESET_ALL}\n{daily['data']}\n")

    if weekdays == 3:
        output.append(f"\n{Fore.GREEN}--疯狂星期四--{Style.RESET_ALL}\n{kfc['data']}")

    output.append(f"\n{Back.CYAN}@yunus0906{Style.RESET_ALL} https://github.com/yunus0906/slack-fish")
    return "\n".join(output)

def main_for_html():

    GITHUB_BUTTON = """
        <!-- Place this tag where you want the button to render. -->
        <a class="github-button" href="https://github.com/yunus0906/slack-fish" data-icon="octicon-star" data-show-count="true" aria-label="Star yunus0906/slack-fish on GitHub">slack-fish</a>
        """

    output = []
    
    current_date, current_weekday, weekdays = get_current_date()
    output.append("<h2>【摸鱼办】提醒您：</h2>")
    output.append(f"<p>今天是 <span style='color: cyan;'>{current_date}</span>，{current_weekday}</p>")
    greeting = get_greeting()
    output.append(f"<p>{greeting}！摸鱼人！工作再累，一定不要忘记摸鱼哦！<br>有事没事起身去茶水间，去厕所，去廊道走走别老在工位上坐着，钱是老板的，但命是自己的🏃‍♀️‍➡️</p>")

    saturday = datetime.now() + timedelta((5 - datetime.now().weekday()) % 7)
    output.append(f"<p>距离【周六】还有：{get_days_until(saturday.date())}天</p>")

    holidays = get_next_public_holidays()
    for holiday in holidays:
        output.append(f"<p>距离【{holiday['localName']}】还有：{get_days_until(datetime.strptime(holiday['date'], '%Y-%m-%d').date())}天</p>")

    daily = get_daily()
    kfc = get_kfc_v_wo50()
    output.append(f"<h3 style='color: green;'>--每日一言--</h3><p>{daily['data']}</p>")

    if weekdays == 3:
        output.append(f"<h3 style='color: green;'>--疯狂星期四--</h3><p>{kfc['data']}</p>")

    output.append(
        f"{GITHUB_BUTTON}"
    )
    return "".join(output)