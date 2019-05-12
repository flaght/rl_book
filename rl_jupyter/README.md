### 获取数据
**注意：query函数的更多用法详见:** [sqlalchemy.orm.query.Query对象](https://docs.sqlalchemy.org/en/rel_1_0/orm/query.html)


获取股票的资产负债数据、现金流数据、利润数据、财务指标数据，行情数据，指数成分股数据等。详情通过数据结构列表查看!

#### 调用方式
```python
	get_fundamentals(query_object, date=None)
```
- 传入date时, 查询指定日期date所能看到的数据.

1. 由于公司发布财报不及时, 一般是看不到当季度财务报表的.
2. 由于每天更新, 当按季度或者年份查询时, 返回季度或者年份最后一天的数据.

#### 参数
- query_object: 一个sqlalchemy.orm.query.Query对象, 可以通过全局的query函数获取Query对象，query简易教程。
- date: 查询日期, 一个字符串(格式类似’2015-10-15’)或者[datetime.date]/[datetime.datetime]对象, 可以是None, 使用默认日期.

#### 返回
返回一个[pandas.DataFrame], 每一行对应数据库返回的每一行(可能是几个表的联合查询结果的一行), 列索引是你查询的所有字段。
1.当相关股票上市前、退市后，财务数据返回各字段为空.

示例

``` python
 # 查询'000008.XSHE'的所有现金流数据, 时间是2018-11-28
q = query(CashFlow).filter(
    CashFlow.trade_date == ’2018-11-28‘
    CashFlow.symbol==('000008.XSHE'))
get_fundamentals(q)
```

``` python
q = query(CashFlow).filter(
    CashFlow.trade_date = ’2018-11-28‘
    # 这里不能使用 in 操作, 要使用in_()函数
    CashFlow.symbol.in_(['000008.XSHE','000009.XSHE']))
get_fundamentals(q)
```
```python
  # 选出所有的销售商品，提供劳务收到的现金大于1000000元, 市盈率小于10, 
  # 营业总收入大于200亿元的股票
    df = get_fundamentals(query(
          Valuation.symbol, CashFlow.goods_sale_and_service_render_cash, Valuation.pe_ratio,
          Income.total_operating_revenue
      ).filter(
          CashFlow.goods_sale_and_service_render_cash > 1000000,
          Valuation.pe_ratio < 10,
          Income.total_operating_revenue > 2e10
      ).order_by(
          # 按市值降序排列
          Valuation.market_cap.desc()
      ).limit(
          # 最多返回100个
          100
      ), date='2015-10-15')	
```
```python
# 可自行导入sqlalchemy中的库使用
# 使用 or_ 函数: 查询总市值大于1000亿元 **或者** 市盈率小于10的股票
  from sqlalchemy.sql.expression import or_
  get_fundamentals(query(
          valuation.code
      ).filter(
          or_(
              valuation.market_cap < 1000,
              valuation.pe_ratio > 10
          )
      ))
```

## 更多使用方法请参照提供的demo例子