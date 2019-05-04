## 数据库调用方式
> query函数的更多用法详见：[sqlalchemy.orm.query.Query](https://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)对象

### 获取数据
#### 1.引入库
``` python
from vision.api import *
```
##### 2.获取数据
##### 2.1 中证500成分股
``` python
q = query(Index.isymbol, Index.trade_date,Index.iname,
         Index.symbol,Index.sname,Index.weighing).filter(
    Index.trade_date < '2019-01-08', Index.trade_date > '2018-01-01', Index.isymbol=='000905.XSHG')
index_df = get_fundamentals(q)
```

##### 2.2 获取指定成分股现金流数据
```python
q = query(CashFlow.symbol, CashFlow.trade_date, CashFlow.net_operate_cash_flow,
         CashFlow.net_invest_cash_flow, CashFlow.net_finance_cash_flow).filter(
    CashFlow.trade_date < '2019-01-08', CashFlow.trade_date > '2017-01-01',
    CashFlow.symbol.in_ (list(set(index_df.symbol))))
cash_flow = get_fundamentals(q)
```

##### 2.3 获取指定成分股获取涨跌幅
```python
q = query(SkDailyPrice.symbol, SkDailyPrice.trade_date,SkDailyPrice.change_pct).filter(
    SkDailyPrice.trade_date < '2019-01-08', SkDailyPrice.trade_date > '2017-01-01', 
    SkDailyPrice.symbol.in_ (list(set(index_df.symbol))))
dx_df = get_fundamentals(q)
```

### 更多获取数据方式参照 数据说明 文档