### 数据处理
接口名 || 说明
---|---|---
winsorize  | [data/winsorize](data/winsorize.html) | 去极值
standardize | [data/standardize](data/standardize.html)| 标准化
neutralize | [data/neutralize](data/neutralize.html)| 中性化
factor_processing | [data/factor_processing](data/factor_processing.html)| 集成化处(包含去极大值，标准化，中性化)
rank | [data/rank](data/rank.html)| 从小到大排序，返回序列值
quantile | [data/quantile](data/quantile.html)| 从小到大顺序进行分组，返回每个因子属于的组别
percentile | [data/percentile](data/percentile.html)| 元素的百分位

### 组合优化
接口名 || 说明
---|---|---
linear_builder|[portfolio/linear_builder](portfolio/linear_builder.html)|线型优化
mean_variance_builder|[portfolio/mean_variance_builder](portfolio/mean_variance_builder.html)|均值方差优化

### 交易日历
接口名 || 说明
---|---|---
is_biz_day|[date/is_biz_day](date/is_biz_day.html)|是否是交易日
dates_list|[date/dates_list](date/dates_list.html)|获取日历
biz_dates_list|[date/biz_dates_list](date/biz_dates_list.html)|获取交易日日历
hol_dates_list|[date/hol_dates_list](date/hol_dates_list.html)|获取日历类别
advance_date|[date/advance_date](date/advance_date.html)|指定日期推算交易日
advance_date_by_calendar|[date/advance_date_by_calendar](date/advance_date_by_calendar.html)|指定日期推算交易日
nth_week_day|[date/nth_week_day](date/nth_week_day.html)|计算指定年月和当月星期数获取日期
make_schedule|[date/make_schedule](date/make_schedule.html)|构建交易日集合


---
#### 测试样例下载:

语言 | 下载地址
---|---
python| [点击下载](client.py)