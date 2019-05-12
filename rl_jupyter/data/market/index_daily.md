#### 指数日行情
##### 每天更新(不复权)
##### 表名 IndexDailyPrice
> 返回指定日期行情的情况，包括开盘价，收盘价，成交量等

列名  | 列的含义 | 解释
---|---|---
id|id
symbol|股票代码
trade\_date| 交易日
name|股票名称
pre\_close|前收盘价
close|今收盘价
open|今开盘价
high|最高价
low|最低价
volume|成交量
money|成交金额
deals|成交笔数
avg|当日均价
change|涨跌
change\_pct|涨跌幅
tot\_mkt\_cap|总市值



#### 调用方式

``` python
from vision.api import *
stock_pool = ['000001.XSHE','000002.XSHE','000003.XSHE']

q = query(IndexDailyPrice.symbol, IndexDailyPrice.trade_date,
	IndexDailyPrice.change_pct).filter(
	IndexDailyPrice.trade_date < '2019-01-08', 
	IndexDailyPrice.trade_date > '2017-01-01', 
	IndexDailyPrice.symbol.in_ (list(set(index_df.symbol))))
	
get_fundamentals(q)
```

> query, get_fundamentals调用方式参照
