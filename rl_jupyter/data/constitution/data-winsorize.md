### data/winsorize
去极值

### URL
http://api.crystal.irongliang.com/data/v1/winsorize

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
data_sets|true| object|需要去极值的数据集，必选用json的list格式
num_stds|true| int|标准差倍数

### 注意事项

### 调用样例及调试工具
```python
# 代码样例
```
[测试工具] (http://irongliang.com/)
### 返回结果集
```json
{
    "code": 200,
    "result": "[23189000000.0,23189000000.0,19153000000.0,19153000000.0,
12554000000.0,12554000000.0,6214000000.0,6214000000]"
}
```

关于错误返回值与错误代码，参见[错误代码说明] (http://irongliang.com/)

字段名|字段类型| 字段说明
---|---|---|
code  | int |操作结果
result | object | 去极值后结果

### 其他
### 相关问题