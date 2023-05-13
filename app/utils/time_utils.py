import pandas as pandas


def get_start_and_end_timestamp_by_year_month(start, end):
    """
    根据给定的两个年月字符串，给出各个月份开始的时间戳和结束的时间戳
    :param start: 开始的时间 2023-05
    :param end: 结束的时间  2023-05
    :return: 开始和结束的时间戳
    """
    result = []
    for t in pandas.period_range(start=start, end=end, freq="M").array:
        st = t.start_time
        et = t.end_time
        print(f"{st} | {int(st.timestamp() * 1000)} ~ {et} | {int(et.timestamp() * 1000)}")
        time = {
            'start_timestamp': int(st.timestamp()),
            'end_timestamp': int(et.timestamp())
        }
        result.append(time)
    return result
