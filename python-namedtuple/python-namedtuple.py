from collections import namedtuple

OldChainInfo = namedtuple('OldChainInfo', 'chain client fastlane_dest') 
NewChainInfo = namedtuple('NewChainInfo', ['chain', 'band', 'client', 'radionet_dest'])

if __name__ == '__main__':
    o = OldChainInfo(chain="chain", client="client", fastlane_dest="fastlane_dest")
    print(o.band)