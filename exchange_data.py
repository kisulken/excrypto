import math
import time


def truncate(number, digits) -> float:
    stepper = pow(10.0, digits)
    return math.trunc(stepper * number) / stepper


class ExchangeRate:
    def __init__(self, bid=None, ask=None, dif=None, size=None, sizemul=None, ex1=None, ex2=None):
        self.bid = bid
        self.ask = ask
        self.dif = dif
        self.size = size
        self.sizemul = sizemul;
        self.exchange1 = ex1
        self.exchange2 = ex2
        self.timestamp = time.time()

    def is_profitable(self):
        return self.dif > 0

    def print(self):
        print("bid", "{0:.15f}".format(round(self.bid, 15)))
        print("ask", "{0:.15f}".format(round(self.ask, 15)))
        if self.is_profitable():
            print("dif", "{0:.15f}".format(round(self.dif, 15)))
            print("size", "{0:.15f}".format(round(self.size, 15)))
            print("sizemul", "{0:.15f}".format(round(self.sizemul, 15)))


class Exchange:
    def __init__(self, identifier=None, ask=None, ask_size=None, bid=None, bid_size=None,
                 sym1=None, sym2=None, gateway=None):
        self.identifier = identifier  # exchanger api identifier
        self.gateway = gateway  # exchanger api gateway
        self.ask = ask
        self.ask_size = ask_size;
        self.bid = bid
        self.bid_size = bid_size;
        self.sym1 = sym1
        self.sym2 = sym2

    def compare(self, ex):
        dif = self.bid - ex.ask
        min_size = min(self.bid_size, ex.ask_size)
        sizemul = truncate(min_size * dif, 14)
        return ExchangeRate(self.bid, ex.ask, dif, min_size, sizemul, self, ex)

    def print(self):
        print("identifier", self.identifier)
        print("bid", "{0:.15f}".format(round(self.bid, 15)))
        print("bid_size", "{0:.15f}".format(round(self.bid_size, 15)))
        print("ask", "{0:.15f}".format(round(self.ask, 15)))
        print("ask_size", "{0:.15f}".format(round(self.ask_size, 15)))
