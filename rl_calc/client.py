# coding:utf-8
import pdb
import requests
import json
import numpy as np
import pandas as pd
import importlib

HOST = 'http://192.168.199.137:5001'

class Date(object):
    @classmethod
    def is_biz_day(cls):
        url = HOST + '/date/v1/is_biz_day'
        params = ['china.sse','2018-03-28']
        result = requests.post(url,data={'params':json.dumps(params)},
                       headers={'Content-Type':'application/x-www-form-urlencoded'})
        return(result.text)
    
    @classmethod
    def dates_list(cls):
        url = HOST + '/date/v1/dates_list'
        params = ['2017-03-25','2017-04-01']
        result = requests.post(url,data={'params':json.dumps(params)},
                       headers={'Content-Type':'application/x-www-form-urlencoded'})
        return(result.text)
    
    @classmethod
    def biz_dates_list(cls):
        url = HOST + '/date/v1/biz_dates_list'
        params = ['china.sse', '2017-03-25','2017-04-10']
        result = requests.post(url,data={'params':json.dumps(params)},
                       headers={'Content-Type':'application/x-www-form-urlencoded'})
        return(result.text)
    
    @classmethod
    def hol_dates_list(cls):
        url = HOST + '/date/v1/hol_dates_list'
        params = ['china.sse', '2017-03-25','2017-04-10', 1]
        result = requests.post(url,data={'params':json.dumps(params)},
                       headers={'Content-Type':'application/x-www-form-urlencoded'})
        return(result.text)
    
    @classmethod
    def advance_date(cls):
        url = HOST + '/date/v1/advance_date'
        params = ['2017-03-25', -10]
        result = requests.post(url,data={'params':json.dumps(params)},
                       headers={'Content-Type':'application/x-www-form-urlencoded'})
        return(result.text)
    
    @classmethod
    def advance_date_by_calendar(cls):
        url = HOST + '/date/v1/advance_date_by_calendar'
        params = ['china.sse', '2017-03-25', '-6m']
        result = requests.post(url,data={'params':json.dumps(params)},
                       headers={'Content-Type':'application/x-www-form-urlencoded'})
        return(result.text)
    
    @classmethod
    def nth_week_day(cls):
        url = HOST + '/date/v1/nth_week_day'
        params = [2,5,6,2018]
        result = requests.post(url,data={'params':json.dumps(params)},
                       headers={'Content-Type':'application/x-www-form-urlencoded'})
        return(result.text)
    
    @classmethod
    def make_schedule(cls):
        url = HOST + '/date/v1/make_schedule'
        params = ['2018-01-04','2018-12-23','10b','china.sse']
        result = requests.post(url,data={'params':json.dumps(params)},
                       headers={'Content-Type':'application/x-www-form-urlencoded'})
        return(result.text)
        
        
class Data(object):
    @classmethod
    def winsorize(cls):
        url = HOST + '/data/v1/winsorize'
        sets = np.random.rand(300, 1)
        num_stds = 2
        result = requests.post(url,data={'data_sets':json.dumps(sets.tolist()), 'num_stds':num_stds},
                       headers={'Content-Type':'application/x-www-form-urlencoded'})
        return(result.text)
        
    @classmethod
    def standardize(cls):
        url = HOST +'/data/v1/standardize'
        sets = np.random.rand(50, 1)
        result = requests.post(url,data={'data_sets':json.dumps(sets.tolist())},
                       headers={'Content-Type':'application/x-www-form-urlencoded'})
        return(result.text)
    
    @classmethod
    def neutralize(cls):
        url = HOST + '/data/v1/neutralize'
        raw_factors = np.random.rand(30, 10)
        risk_factors = np.random.rand(30, 4)
        result = requests.post(url,data={'data_sets':json.dumps(raw_factors.tolist()),
                                     'benchmark_sets':json.dumps(risk_factors.tolist())},
                       headers={'Content-Type':'application/x-www-form-urlencoded'})
        return(result.text)

    @classmethod
    def factor_processing(cls):
        url = HOST + '/data/v1/factor_processing'
        raw_factors = np.random.rand(30, 10)
        risk_factors = np.random.rand(30, 4)
        result = requests.post(url,data={'data_sets':json.dumps(raw_factors.tolist()),
                                     'benchmark_sets':json.dumps(risk_factors.tolist())},
                       headers={'Content-Type':'application/x-www-form-urlencoded'})
        return(result.text)

    @classmethod
    def rank(cls):
        url = HOST + '/data/v1/rank'
        raw_factors = np.random.rand(10, 1)
        result = requests.post(url,data={'data_sets':json.dumps(raw_factors.tolist())},
                       headers={'Content-Type':'application/x-www-form-urlencoded'})
        return(result.text)
    
    @classmethod
    def quantile(cls):
        url = HOST + '/data/v1/quantile'
        raw_factors = np.random.rand(10, 1).flatten()
        result = requests.post(url,data={'data_sets':json.dumps(raw_factors.tolist()),
                                    'n_bins':5},
                       headers={'Content-Type':'application/x-www-form-urlencoded'})
        return(result.text)
    
    @classmethod
    def percentile(cls):
        url = HOST + '/data/v1/percentile'
        raw_factors = np.random.rand(10, 1).flatten()
        result = requests.post(url,data={'data_sets':json.dumps(raw_factors.tolist())},
                       headers={'Content-Type':'application/x-www-form-urlencoded'})
        return(result.text)

class Portfolio(object):
    @classmethod
    def linear_builder(cls):
        n = 5
        url = HOST + '/portfolio/v1/linear_builder'
        expect_return = np.random.randn(n)
        weight_lb = np.zeros(n)
        weight_ub = 0.5 * np.ones(n)
        risk_factors = np.ones((n, 1))
        risk_lbound = np.ones(1)
        risk_ubound = np.ones(1)
        turn_over_target = 0.1
        current_pos = np.random.randint(0, n, size=n)
        current_pos = current_pos / current_pos.sum() 
        result = requests.post(url,data={'expect_return':json.dumps(expect_return.tolist()),
                                        'weight_lb':json.dumps(weight_lb.tolist()),
                                        'weight_ub':json.dumps(weight_ub.tolist()),
                                        'risk_factors':json.dumps(risk_factors.tolist()),
                                        'risk_lbound':json.dumps(risk_lbound.tolist()),
                                        'risk_ubound':json.dumps(risk_ubound.tolist()),
                                        'turn_over_target':turn_over_target,
                                        'weight':json.dumps(current_pos.tolist())},
                       headers={'Content-Type':'application/x-www-form-urlencoded'})
        return(result.text)
    
    @classmethod
    def mean_variance_builder(cls):
        url = HOST + '/portfolio/v1/mean_variance_builder'
        expect_return = np.array([0.1, 0.2, 0.3])
        cov = np.array([[0.02, 0.01, 0.02],
                [0.01, 0.02, 0.03],
                [0.02, 0.03, 0.02]])
        ids_var = np.diag([0.01, 0.02, 0.03])
        cov += ids_var
        risk_exposure = np.array([[1., 1., 1.],
                         [1., 0., 1.]]).T
        bm = np.array([0.3, 0.3, 0.4])
        lbound = np.array([0., 0., 0.])
        ubound = np.array([0.4, 0.4, 0.5])
        lrisk_target = np.array([bm.sum(), 0.3])
        urisk_target = np.array([bm.sum(), 0.7])
        #risk_target = (np.array([bm.sum(), 0.3]).tolist(), np.array([bm.sum(), 0.7]).tolist())
        result = requests.post(url,data={'expect_return':json.dumps(expect_return.tolist()),
                                        'bm':json.dumps(bm.tolist()),
                                        'lbound':json.dumps(lbound.tolist()),
                                        'ubound':json.dumps(ubound.tolist()),
                                        'risk_exposure':json.dumps(risk_exposure.tolist()),
                                        'lrisk_target':json.dumps(lrisk_target.tolist()),
                                        'urisk_target':json.dumps(urisk_target.tolist()),
                                        'cov':json.dumps(cov.tolist())},
                               headers={'Content-Type':'application/x-www-form-urlencoded'})
        return(result.text)
    
 



if __name__ == '__main__':
    date = Date()
    print(date.advance_date_by_calendar())