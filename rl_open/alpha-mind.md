# Alpha - Mind

**Alpha - Mind** 是基于 **Python** 开发的股票多因子研究框架。

## 依赖

该项目主要有两个主要的github外部依赖：

* portfolio - optimizer 该项目是相同作者编写的用于资产组合配置的优化器工具包；

* xgboost 该项目是alpha - mind中一些机器模型的基础库。

这两个库都已经使用git子模块的方式打包到alpha-mind代码库中。

## 功能

alpha - mind 提供了多因子研究中常用的工具链，包括：

* 数据清洗
* alpha 模型
* 风险模型
* 组合优化
* 执行器

所有的模块都设计了完整的测试用例以尽可能保证正确性。同时，所有的数值模型开发中都对性能给予了足够高的关注，参考了优秀的第三方工具以保证性能：

* numpy
* numba
* cvxopt
* cvxpy
* pandas
* scipy

