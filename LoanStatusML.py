#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 13 16:01:55 2021

@author: ethanmitten
"""

import pandas as pd
import matplotlib.pyplot as plt

#%%
train = pd.read_csv('/Users/ethanmitten/Desktop/Data Analytics/Python Projects/LoanStatusDataset/train_loanstatus.csv')
test = pd.read_csv('/Users/ethanmitten/Desktop/Data Analytics/Python Projects/LoanStatusDataset/test_loanstatus.csv')

#%%
train.info()
#%%
#plt.hist(train['ApplicantIncome']) #Will need to do a log transformation on this column
#plt.hist(train['CoapplicantIncome']) #Will need to do a log transformation on this column
#plt.hist(train['LoanAmount']) #Will need to do a log transformation on this column
#plt.hist(train['Loan_Amount_Term'])
#plt.hist(train['Credit_History'])
train.Married.value_counts()

#Will need to apply log transformations on the test columns ApplicantIncome, CoapplicantIncome and LoanAmount

#%%
