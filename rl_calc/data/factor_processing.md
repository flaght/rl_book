### data/factor_processing
中性化

### URL
http://api.crystal.irongliang.com/data/v1/factor_processing

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
benchmark_sets|true| object| 中性化基准数据集
data_sets|true| object|需要去极值的数据集，必选用json的list格式

### 返回结果集
```json
{
    "code": 200,
    "result": "[0.23189,0.19153, 0.12554,0.42554,0.6214,0.6314]"
}
```

字段名|字段类型| 字段说明
---|---|---|
code  | int |操作结果
result | object | 处理后的结果