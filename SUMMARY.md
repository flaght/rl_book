# 融量平台帮助文档

* 1. [融量介绍](README.md)
* 2. 融量量化平台说明文档
    * 数据说明
    	* 财务数据
    		* 报表期更新
    			* [财务指标](rl_jupyter/data/finance/report_update/indicator.md)
    			* [利润数据](rl_jupyter/data/finance/report_update/income.md) 
    			* [现金流数据](rl_jupyter/data/finance/report_update/cash_flow.md) 
    			* [资产负债数据](rl_jupyter/data/finance/report_update/balance.md) 
    		* 每日更新
    			* [市值数据表](rl_jupyter/data/finance/every_update/valuation.md)
    			* [财务指标](rl_jupyter/data/finance/every_update/indicator.md)
    			* [利润数据](rl_jupyter/data/finance/every_update/income.md) 
    			* [现金流数据](rl_jupyter/data/finance/every_update/cash_flow.md)  
    			* [资产负债数据](rl_jupyter/data/finance/every_update/balance.md) 
    			* [母公司利润表](rl_jupyter/data/finance/every_update/stk_income_statement_parent.md)
    			* [母公司现金流量表](rl_jupyter/data/finance/every_update/stk_cashflow_statement_parent.md)
    			* [母公司资产负债表](rl_jupyter/data/finance/every_update/stk_balance_statement_parent.md)
    	* 行情数据
    		* [股票日行情](rl_jupyter/data/market/stock_daily.md)
    		* [指数日行情](rl_jupyter/data/market/index_daily.md)
    	* 成分股
    		* [行业成分股](rl_jupyter/data/constitution/industry.md)
    		* [指数成分股](rl_jupyter/data/constitution/index.md) 
    * 接口说明
    	* 数据调用接口
    		* [数据库调用](rl_jupyter/interface/db.md)
    		* [本地文件调用](rl_jupyter/interface/file.md) 
    * [例子说明](rl_jupyter/example/Quick_Start_2.md)
* 3. [融量计算HTTP API说明文档](rl_calc/interface_help.md)
	* [数据处理接口](rl_calc/interface_help.md)
		* [winsorize](rl_calc/data/winsorize.md)
		* [standardize](rl_calc/data/standardize.md)
		* [neutralize](rl_calc/data/neutralize.md)
		* [factor_processing](rl_calc/data/factor_processing.md)
		* [rank](rl_calc/data/rank.md)
		* [quantile](rl_calc/data/quantile.md)
		* [percentile](rl_calc/data/percentile.md)
	* [日期计算接口](rl_calc/interface_help.md)
		* [is_biz_day](rl_calc/date/is_biz_day.md)
		* [dates_list](rl_calc/date/dates_list.md) 
		* [biz_dates_list](rl_calc/date/biz_dates_list.md) 
		* [hol_dates_list](rl_calc/date/hol_dates_list.md)
		* [advance_date](rl_calc/date/advance_date.md)
		* [advance_date_by_calendar](rl_calc/date/advance_date_by_calendar.md)
		* [nth_week_day](rl_calc/date/nth_week_day.md)
		* [make_schedule](rl_calc/date/make_schedule.md)
	* [组合优化接口](rl_calc/interface_help.md)
		* [linear_builder](rl_calc/portfolio/linear_builder.md)
		* [mean_variance_builder](rl_calc/portfolio/mean_variance_builder.md) 
* 4. [融量开源项目](rl_open/README.md)
	* [alpha-mind](rl_open/alpha-mind.md)
	* [Finance-Python](rl_open/Finance-Python.md)
	* [fantatic](rl_open/fantatic.md)
	* [BasicCore](rl_open/BasicCore.md)
	* [mylib](rl_open/mylib.md)