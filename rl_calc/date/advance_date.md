### date/advance_date
指定日期推算交易日

### URL
http://api.crystal.irongliang.com/date/v1/advance_date

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
params|true| object| 参数值集 list格式， 0 交易日 为格式为'2019-12-24'  1.间隔日，正数向后计算 负数向前计算

### 返回结果集
```json
{
  "code": 200,
  "result": [
    "2017-03-25"
  ]
}
```

字段名|字段类型| 字段说明
---|---|---|
code  | int |操作结果
result | object  | 推算出的日期