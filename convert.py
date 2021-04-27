from forex_python.converter import CurrencyCodes, CurrencyRates
from forex_python.bitcoin import BtcConverter


CC = CurrencyCodes()
CR = CurrencyRates(force_decimal=True)
BT = BtcConverter()

def converter(input_code, output_code, amount):
    return CR.convert(input_code,output_code, amount)