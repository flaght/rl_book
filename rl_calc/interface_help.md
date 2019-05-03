### 数据处理
接口名 || 说明
---|---|---
winsorize  | [data/winsorize](data/winsorize.md) | 去极值
standardize | [data/standardize](http://git.irongliang.com/KerryDong/open_crystal/wikis/data/standardize)| 标准化
neutralize | [data/neutralize](http://git.irongliang.com/KerryDong/open_crystal/wikis/data/neutralize)| 中性化
factor_processing | [data/factor_processing](http://git.irongliang.com/KerryDong/open_crystal/wikis/data/factor_processing)| 集成化处(包含去极大值，标准化，中性化)
rank | [data/rank](http://git.irongliang.com/KerryDong/open_crystal/wikis/data/rank)| 从小到大排序，返回序列值
quantile | [data/quantile](http://git.irongliang.com/KerryDong/open_crystal/wikis/data/quantile)| 从小到大顺序进行分组，返回每个因子属于的组别
percentile | [data/percentile](http://git.irongliang.com/KerryDong/open_crystal/wikis/data/percentile)| 元素的百分位

### 组合优化
接口名 || 说明
---|---|---
linear_builder|[portfolio/linear_builder](http://git.irongliang.com/KerryDong/open_crystal/wikis/portfolio/linear_builder)|线型优化
mean_variance_builder|[portfolio/mean_variance_builder](http://git.irongliang.com/KerryDong/open_crystal/wikis/portfolio/mean_variance_builder)|均值方差优化

### 交易日历
接口名 || 说明
---|---|---
is_biz_day|[date/is_biz_day](http://git.irongliang.com/KerryDong/open_crystal/wikis/date/is_biz_day)|是否是交易日
dates_list|[date/dates_list](http://git.irongliang.com/KerryDong/open_crystal/wikis/date/dates_list)|获取日历
biz_dates_list|[date/biz_dates_list](http://git.irongliang.com/KerryDong/open_crystal/wikis/date/biz_dates_list)|获取交易日日历
hol_dates_list|[date/hol_dates_list](http://git.irongliang.com/KerryDong/open_crystal/wikis/date/hol_dates_list)|获取日历类别
advance_date|[date/advance_date](http://git.irongliang.com/KerryDong/open_crystal/wikis/date/advance_date)|指定日期推算交易日
advance_date_by_calendar|[date/advance_date_by_calendar](http://git.irongliang.com/KerryDong/open_crystal/wikis/date/advance_date_by_calendar)|指定日期推算交易日
nth_week_day|[date/nth_week_day](http://git.irongliang.com/KerryDong/open_crystal/wikis/date/nth_week_day)|计算指定年月和当月星期数获取日期
make_schedule|[date/make_schedule](http://git.irongliang.com/KerryDong/open_crystal/wikis/date/make_schedule)|构建交易日集合
