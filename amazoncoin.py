import time
import pyupbit
import datetime



def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

def get_ma24(ticker):
    """24시간 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="minute1", count=1*60)
    ma24 = df['close'].rolling(1*60).mean().iloc[-1]
    return ma24

#현재가 이동평균 차이
def ma_current_gap(ticker): 
    gap=(get_current_price(ticker)/get_ma24(ticker)*100)  # 현재가/평균 *100
    return gap

#저가 매수 코인 선정
def find_coin():
    gap=[]
    for k in tickerk:
        gap.append(get_current_price(k)/get_ma24(k)*100)
        minus_big_gap=min(gap)
        position=gap.index(minus_big_gap)
        if position==0:
          val=tickerk[0]
        elif position==1:
          val=tickerk[1]
        elif position==2:
          val=tickerk[2]
        elif position==3:
          val=tickerk[3]   
        elif position==4:
          val=tickerk[4]
        elif position==5:
          val=tickerk[5]
        elif position==6:
          val=tickerk[6]      
        elif position==7:
          val=tickerk[7]   
        elif position==8:
          val=tickerk[8]
        elif position==9:
          val=tickerk[9]
        elif position==10:
          val=tickerk[10]        
        elif position==11:
          val=tickerk[11]      
        elif position==12:
          val=tickerk[12]   
        elif position==13:
          val=tickerk[13]
        elif position==14:
          val=tickerk[14]
        elif position==15:
          val=tickerk[15]   
        time.sleep(0.1)       
    return val

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="minute60", count=2)
    start_time = df.index[0]
    return start_time

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def coin_name(ticker):
    if ticker=="KRW-FLOW":
        s="FLOW"
    elif ticker=="KRW-DKA":
        s="DKA"
    elif ticker=="KRW-EOS":
        s="EOS"
    elif ticker=="KRW-ADA":
        s="ADA"
    elif ticker=="KRW-ETC":
        s="ETC"
    elif ticker=="KRW-TRX":
        s="TRX"
    elif ticker=="KRW-QTUM":
        s="QTUM"
    elif ticker=="KRW-DOGE":
        s="DOGE"
    elif ticker=="KRW-BTC":
        s="BTC"
    elif ticker=="KRW-UPP":
        s="UPP"
    elif ticker=="KRW-ARK":
        s="ARK"
    elif ticker=="KRW-CVC":
        s="CVC"
    elif ticker=="KRW-MOC":
        s="MOC"
    elif ticker=="KRW-BORA":
        s="BORA"
    elif ticker=="KRW-XLM":
        s="XLM"
    elif ticker=="KRW-ARDR":
        s="ARDR"
    elif ticker=="KRW-TON":
        s="TON"
    elif ticker=="KRW-HIVE":
        s="HIVE"
    elif ticker=="KRW-XEM":
        s="XEM"
    elif ticker=="KRW-SC":
        s="SC"
    elif ticker=="KRW-META":
        s="META"
    elif ticker=="KRW-ONG":
        s="ONG"
    elif ticker=="KRW-XTZ":
        s="XTZ"
    elif ticker=="KRW-MTL":
        s="MTL"
    elif ticker=="KRW-ANKR":
        s="ANKR"
    elif ticker=="KRW-LSK":
        s="LSK"
    elif ticker=="KRW-POWR":
        s="POWR"
    elif ticker=="KRW-MVL":
        s="MVL"
    elif ticker=="KRW-SSX":
        s="SSX"
    elif ticker=="KRW-ENJ":
        s="ENJ"
    elif ticker=="KRW-WAXP":
        s="WAXP"
    elif ticker=="KRW-GAS":
        s="GAS"
    elif ticker=="KRW-STMX":
        s="STMX"
    elif ticker=="KRW-ONT":
        s="ONT"
    elif ticker=="KRW-STRK":
        s="STRK"
    elif ticker=="KRW-REP":
        s="REP"
    elif ticker=="KRW-IOTA":
        s="IOTA"
    elif ticker=="KRW-STEEM":
        s="STEEM"
    elif ticker=="KRW-CRO":
        s="CRO"
    elif ticker=="KRW-ICX":
        s="ICX"
    elif ticker=="KRW-PLA":
        s="PLA"   
    elif ticker=="KRW-ETH":
        s="ETH"
    elif ticker=="KRW-NEO":
        s="NEO"
    elif ticker=="KRW-POLY":
        s="POLY"
    elif ticker=="KRW-MED":
        s="MED"
    elif ticker=="KRW-DAWN":
        s="DAWN"        
    elif ticker=="KRW-BCH":
        s="BCH"
    elif ticker=="KRW-ELF":
        s="ELF"
    elif ticker=="KRW-LOOM":
        s="LOOM"       
    elif ticker=="KRW-LINK":
        s="LINK"
    elif ticker=="KRW-STRAX":
        s="STRAX"       
    elif ticker=="KRW-BTT":
        s="BTT"
    elif ticker=="KRW-VET":
        s="VET"
    elif ticker=="KRW-SXP":
        s="SXP"       
    elif ticker=="KRW-KAVA":
        s="KAVA"
    elif ticker=="KRW-XRP":
        s="XRP"      
    elif ticker=="KRW-TT":
        s="TT"       
    elif ticker=="KRW-CRE":
        s="CRE"
    elif ticker=="KRW-HUM":
        s="HUM"         
    elif ticker=="KRW-LTC":
        s="LTC"
    elif ticker=="KRW-BSV":
        s="BSV"            
    elif ticker=="KRW-QKC":
        s="QKC"
    elif ticker=="KRW-IOST":
        s="IOST"
                          
    return s
#수정

tickerk=("KRW-LINK","KRW-EOS","KRW-ADA","KRW-ETC","KRW-BSV","KRW-LTC","KRW-BTC",
"KRW-DOGE","KRW-NEO","KRW-BTC","KRW-CRO","KRW-GAS")

access = "xxx"
secret = "xxx"

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

si=21
buy_ma_gap=94
sell_ma_gap=103


while True:
    
    ticker=find_coin()  ##min gap 찾는 코드 코딩하기 while
    ma_now_gap=ma_current_gap(ticker)

    if ma_now_gap<buy_ma_gap:   # 급락장 97.5  # 평상시 98.5
        break

# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        current_price = get_current_price(ticker)
        ma_now_gap=ma_current_gap(ticker)
        ma24 = get_ma24(ticker)
        current_price = get_current_price(ticker)

        if ma_now_gap<95:
            krw = get_balance("KRW")
            if krw > 5000:
                upbit.buy_market_order(ticker, krw*0.9995)
                coindj = get_balance(coin_name(ticker))
                while True:
                    if ma_now_gap > sell_ma_gap:
                        upbit.sell_market_order(ticker, coindj*0.9995)
                        break


        coindj = get_balance(coin_name(ticker))
        now_price=current_price*coindj


        if  ma_now_gap > sell_ma_gap :
            upbit.sell_market_order(ticker, coindj*0.9995)
            
            while True:
                ticker=find_coin() 
                ma_now_gap=ma_current_gap(ticker)
                if ma_now_gap<buy_ma_gap:
                    break

        time.sleep(1)


    except Exception as e:
        print(e)
        time.sleep(1) 
