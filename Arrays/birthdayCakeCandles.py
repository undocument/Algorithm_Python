candle =[4,4,1,3]
def birthdayCakeCandles(candles):
    max_num = max(candles)
    count = candles.count(max_num)
    return count

birthdayCakeCandles(candle)