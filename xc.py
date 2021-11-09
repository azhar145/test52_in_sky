##import talib as ta
##from ta.utils import dropna
import yfinance as yf
from yfinance import Ticker as yf2
import pandas as pd
import sys
##import re
import numpy as np
##from talib import stream

from millify import millify
##today = datetime.date.today() + datetime.timedelta(days=1)
##today = date.date.today()
##day = datetime.datetime.strptime(Date, '%d %m %Y').weekday()
##print(datetime.today().strftime('%Y-%m-%d'))
##import mpl_finance
##import matplotlib
import sys
##from matplotlib.finance import candlestick2_ohlc
##from mpl_finance import candlestick_ohlc
##from mplfinance.original_flavor import candlestick_ohlc

from numerize import numerize
import matplotlib.pyplot as plt
pd.options.display.width = 0
pd.set_option('display.max_columns', None)
pd.options.display.float_format = '{:.2f}'.format
##pd.options.display.max_columns=255
pd.options.display.max_rows=6500000
pd.set_option('display.max_colwidth', 500)
pd.set_option('display.max_columns', 550)
pd.options.mode.chained_assignment = None  # default='warn'
import sys
import re

##global n2,n4,breakz
n2=2
n4=2
##breakz=10000

def test():
    import streamlit as st
    st.legacy_caching.clear_cache()
    
    print("inside test - Earnings_backup22.py")


    readp='/home/az2/t__214.txt'
    write_to='/home/az2/t-215.txt'
    

    
##    print(df,'df info')

    v=0
    f=open(readp, 'r+')
    f2=open(write_to,'w+')
    for x in f:
        f2.write(x.rstrip())
        f2.write('\n')

        v=v+1
        if v > 20:
            break
        print(x)
    f2.close()


    df=pd.read_csv('/home/az2/t-215.txt')
    df=pd.DataFrame(df)
    df.columns=['ticker']
    df['b_recommendationKey']=''
    df['b_sector']=''
    df['b_shortName']=''
    df['b_previousClose']=''
    df['b_fiftyDayAverage']=''
    df['b_regularMarketOpen']=''
    df['b_regularMarketVolume']=''
    df['b_totalCashPerShare']=''
    df['b_volume']=''
    df['b_averageVolume']=''
    df['b_averageVolume10days']=''
    df['b_forwardEps']=''
    df['b_trailingEps']=''

    df['b_totalCash']=''
    df['b_totalDebt']=''
    df['b_totalRevenue']=''
    df['b_totalCashPerShare']=''
    df['b_revenuePerShare']=''
    df['b_earningsQuarterlyGrowth']=''
    df['b_recommendationMean']=''
    df['b_sharesPercentSharesOut']=''

    df['b_swing']=''
    df['Price > 50day_avg']=''
    df['v_earng']=''
       
    ##    df['ms_totalCashPerShare']=''
    df['b_sharesOutstanding']=''
    df['b_sharesShort']=''
    df['b_sharesPercentSharesOut']=''
    df['b_heldPercentInstitutions']=''
    df['b_floatShares']=''
    df['b_shortPercentOfFloat']=''
    df['b_sharesShortPriorMonth']=''
    df['b_dateShortInterest']=''
    df['b_fullTimeEmployees']=''
    df['short_more_now']=''
    df['b_shortRatio']=''

    df['b_sharesShort'] = ''
    df['b_sharesShortPriorMonth']=''
    df['b_short_more_now']=''
    df['b_shortRatio']=''
    df['b_heldPercentInsiders']=''
    df['b_heldPercentInstitutions']=''
    df['b_earningsGrowth']=''
    df['Vol > 10 days_Vol']=''


    i=0
    for x in df.index:
        i=i+1
        print(i,') ',df['ticker'].loc[x])
        df['b_sector'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['sector']
     
        df['b_recommendationKey'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['recommendationKey']
        df['Earning_imprv']= yf.Ticker(df['ticker'].loc[x]).info['forwardEps']-yf.Ticker(df['ticker'].loc[x]).info['trailingEps'] 
        df['b_sector'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['sector']
        df['b_shortName'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['shortName']
           
        df['b_previousClose'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['previousClose']
        df['b_regularMarketVolume'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['regularMarketVolume']
        df['b_volume'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['volume']
        df['Vol > 10 days_Vol']=yf.Ticker(df['ticker'].loc[x]).info['volume']+.01 - yf.Ticker(df['ticker'].loc[x]).info['averageVolume10days']+.01                                                             
        df['b_regularMarketOpen'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['regularMarketOpen']
        df['b_swing'].loc[x]=  df['b_previousClose'].loc[x]- df['b_regularMarketOpen'].loc[x]       
        df['b_fiftyDayAverage'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['fiftyDayAverage']
        df['Price > 50day_avg'].loc[x]= df['b_previousClose'].loc[x]- df['b_fiftyDayAverage'].loc[x] 
        
        df['b_averageVolume'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['averageVolume']
        df['b_averageVolume10days'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['averageVolume10days']                                                                    
        
        
                                                                           
        df['b_totalCashPerShare'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['totalCashPerShare']

        df['b_forwardEps'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['forwardEps']
        df['b_trailingEps'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['trailingEps']
        df['v_earng'].loc[x] = df['b_forwardEps'].loc[x]-df['b_trailingEps'].loc[x]
        df['b_totalCash'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['totalCash']
        df['b_totalDebt'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['totalDebt']
        df['b_totalRevenue'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['totalRevenue']
        df['b_totalCashPerShare'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['totalCashPerShare']
        df['b_revenuePerShare'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['revenuePerShare']
        df['b_earningsQuarterlyGrowth'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['earningsQuarterlyGrowth']
        df['b_earningsGrowth'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['earningsQuarterlyGrowth']
        df['b_recommendationMean'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['earningsGrowth']


        df['b_sharesOutstanding'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['sharesOutstanding']
        
        df['b_sharesPercentSharesOut'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['sharesPercentSharesOut']
        
        df['b_floatShares'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['floatShares']
        df['b_shortPercentOfFloat'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['shortPercentOfFloat']

        df['b_dateShortInterest'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['dateShortInterest']
        df['b_fullTimeEmployees'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['fullTimeEmployees']

        df['b_sharesShort'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['sharesShort']
        df['b_sharesShortPriorMonth'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['sharesShortPriorMonth']
        df['b_short_more_now'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['sharesShort']-yf.Ticker(df['ticker'].loc[x]).info['sharesShortPriorMonth']
        df['b_shortRatio'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['shortRatio']
        df['b_heldPercentInsiders'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['heldPercentInsiders']
        df['b_heldPercentInstitutions'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['heldPercentInstitutions']



####    df['ms_earningsQuarterlyGrowth']=''
####    df['ms_earningsGrowth']=''

    df.to_csv('\home\az2\info3326.csv')
    return df


##
##
##    sys.exit()
####    df.columns=['ticker']
####    
####
##
####    print(df)
####    sys.exit()
##    df['ms_sector']=''
####    df['ms_fullTimeEmployees']=''
####    df['ms_earningsGrowth']=''
####    df['ms_totalCash']=''
####    df['ms_totalDebt']=''
####    df['ms_totalRevenue']=''
##    df['ms_totalCashPerShare']=''
####    df['ms_sharesOutstanding']=''
####    df['ms_sharesShort']=''
####    df['ms_sharesPercentSharesOut']=''
####    df['ms_heldPercentInstitutions']=''
####    df['ms_floatShares']=''
####    df['ms_shortPercentOfFloat']=''
####    df['ms_sharesShortPriorMonth']='
####    df['ms_dateShortInterest']=''
####    df['ms_fullTimeEmployees']=''

####    df['ms_trailingEps']=''
####    df['ms_heldPercentInsiders']=''
####    df['ms_shortRatio']=''

####    df['ms_earningsQuarterlyGrowth']=''
####    df['ms_dateShortInterest']=''

####    df['ms_averageVolume10days']=''
####    df['ms_askSize']=''
####    df['ms_bidSize']=''
##    df['ms_volume']=''
####    df['ms_averageVolume']=''
####    df['ms_regularMarketVolume']=''
####    df['ms_averageVolume10days']=''

##    df['ms_forwardEps']=''
####    df['ms_recommendationMean']=''
####    df['ms_targetMedianPrice']=''
####    df['ms_targetLowPrice']=''
####    df['ms_recommendationKey']=''
####    df['ms_freeCashflow']=''
####    df['ms_sharesOutstanding']=''
##    df['ms_trailingEps']=''
####    df['ms_shortName']=''
####    df['ms_fullTimeEmployees']=''
####    df['ms_forwardEps']=''
####    df['ms_trailingEps']=''
##    df['ms_recommendationKey']=''
####    df['ms_targetMedianPrice']=''
####    df['ms_targetLowPrice']=''
####    df['ms_recommendationMean']=''
##    df['ms_totalCash']=''
##    df['ms_totalDebt']=''
##    df['ms_totalRevenue']=''
####    df['ms_totalCashPerShare']=''
####
####    df['ms_earningsQuarterlyGrowth']=''
####    df['ms_earningsGrowth']=''
####    df['ms_sharesOutstanding']=''
####    df['ms_freeCashflow']=''
####    df['ms_sharesOutstanding']=''
##
####    df['ms_shortName']=''
####    
####from yfinance import Ticker import info as yf
##    i=0
##
##
####
####    for x in df.index:
####            df['volume'].loc[x]=df['volume'].loc[x] 
####        df['totalRevenue'].loc[x]=numerize.numerize(np.float64(df['totalRevenue'].loc[x].item()))
##
##            
##
##
##   
##    
##    for x in df.index:
##        i=i+1
##        if i > breakz:
##            
##            break
####        print(x)    
##            
####        df['ms_sector'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['sector']
####        df['ms_fullTimeEmployees'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['fullTimeEmployees']
####
####        df['ms_sharesShort'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['sharesShort']
####        df['ms_sharesPercentSharesOut'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['sharesPercentSharesOut']
####        df['ms_heldPercentInstitutions'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['heldPercentInstitutions']
####        df['ms_trailingEps'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['trailingEps']
####        df['ms_heldPercentInsiders'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['heldPercentInsiders']
####        df['ms_shortRatio'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['shortRatio']
####        df['ms_floatShares'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['floatShares']
####        
####        df['ms_dateShortInterest'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['dateShortInterest']
####        df['ms_shortPercentOfFloat'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['shortPercentOfFloat']
####        df['ms_sharesShortPriorMonth'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['sharesShortPriorMonth']
####        df['ms_averageVolume10days'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['averageVolume10days']
####        df['ms_askSize'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['askSize']
####        df['ms_bidSize'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['bidSize']
##        df['ms_volume'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['volume']
####        df['ms_averageVolume'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['averageVolume']
####        df['ms_regularMarketVolume'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['regularMarketVolume']
####        df['ms_averageVolume10days'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['averageVolume10days']
####        df['ms_dateShortInterest'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['dateShortInterest']
####
##        df['ms_forwardEps'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['forwardEps']
##        df['ms_trailingEps'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['trailingEps']
##        df['ms_recommendationKey'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['recommendationKey']
####        df['ms_recommendationMean'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['recommendationMean']
####        df['ms_targetMedianPrice'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['targetMedianPrice']
####        df['ms_targetLowPrice'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['targetLowPrice']
####        df['ms_earningsQuarterlyGrowth'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['earningsQuarterlyGrowth']
####        df['ms_earningsGrowth'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['earningsGrowth']
####        df['ms_totalCash'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['totalCash']
##        df['ms_totalDebt'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['totalDebt']
##        df['ms_totalRevenue'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['totalRevenue']
##        df['ms_totalCashPerShare'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['totalCashPerShare']
####        df['ms_sharesOutstanding'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['sharesOutstanding']
####        df['ms_freeCashflow'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['freeCashflow']
####        df['ms_sharesOutstanding'].loc[x] = yf.Ticker(df['ticker'].loc[x]).info['sharesOutstanding']
####
##
##
####        import humanize
##
####    print(numerize.numerize(np.float32(df33['ms_volume'].loc[x]).item())
####        print(df['ms_volume'].loc[x], 'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP')
####        for x in df.index:
######            df['ms_volume'].loc[x]=np.float64(np.float64(df['ms_volume'].loc[x]))/float(6)
####            df['ms_volume'].loc[x]=df['ms_volume'].loc[x]
##            
####            df['ms_volume'].loc[x]=numerize.numerize(np.float64(df['ms_volume'].loc[x].item()))
##            
####            df['ms_volume'].loc[x]=humanize.naturalsize(df['ms_volume'].loc[x])
####            df['ms_volume'].loc[x]=numerize.numerize(np.float32(df['ms_volume'].loc[x]))
####        df['ms_totalDebt'].loc[x]=numerize.numerize(float(df['ms_totalDebt'].loc[x]))
####        df['ms_totalRevenue'].loc[x]=numerize.numerize(float(df['ms_totalRevenue']).loc[x])
####        df['ms_totalRevenue'].loc[x]=numerize.numerize(float(df['ms_totalRevenue']).loc[x])
##
##
####        df33['Diff_Vol'].loc[x]=numerize.numerize(np.float32(df33['Diff_Vol'].loc[x]).item())
##
##            
##    print('\n\n')
##    
##
##
##    print(df)    
##    f.close()
##    print('\n\n')
##    print('*********************************************************************************************')
##    print('test completed')
##    print('*********************************************************************************************')
##    print('\n\n')
##  

p=test()
print(p)
