### date/hol_dates_list
获取指定交易所交易日历

### URL
http://api.crystal.irongliang.com/date/v1/hol_dates_list

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
params|true| object| 参数值集 list格式， 0 交易所类型; 1 开始日期; 2 结束日期; 3. 日期类别 1.交易日 0.非交易日 为格式为'2019-12-24' 

### 返回结果集
```json
{
  "code": 200,
  "result": [
    "2017-03-25",
    "2017-03-26",
    "2017-03-27",
    "2017-03-28",
    "2017-03-29",
    "2017-03-30",
    "2017-03-31",
    "2017-04-01"
  ]
}
```

字段名|字段类型| 字段说明
---|---|---|
code  | int |操作结果
result | object  | 日历集合