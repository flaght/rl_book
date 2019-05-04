### portfolio/linear_builder
线性构造优化

### URL
http://api.crystal.irongliang.com/portfolio/v1/linear_builder

### 支持格式
JSON

### HTTP请求方式
POST FORM-DATA

### 是否需要登录
否
访问授权限 如何[登陆授权](http://irongliang.com/)

### 访问授权登陆
- 访问级别：普通接口
- 频次限制：否
关于频次限制，参见[接口访问权限说明](http://irongliang.com/)

### 请求参数
参数名 | 必选| 类型及范围| 说明
---|---|---|---|
access_token  | true | string|采用OAuth授权方式为必填参数，OAuth授权后获得
uid | true | int| 用户ID
expect_return|true| object| 预期收益
weight_lb|true| object|约束条件1,标的权重的下限
weight_ub|true| object|约束条件1,标的权重的上限
risk_factors|true|object|风险因子
risk_lbound|true|object|约束条件2,组合风险暴露下限
risk_ubound|true|object|约束条件2,组合风险暴露上限
weight|true|object|标的权重
turn_over_target| true| float|仓位调整的换手率
### 返回结果集
```json
{
  "code": 200,
  "optimized_values": 0.9241274727330153,
  "weights": "[0.05000000000029781, 0.14999999999981237, 0.19999999999989448, 0.1999999999998588, 0.4000000000000018]",
  "status": "optimal"
}
```

字段名|字段类型| 字段说明
---|---|---|
code  | int |操作结果
optimized_values | float | 预期收益的负值
weights| object|主动权重
status| float| 优化状态