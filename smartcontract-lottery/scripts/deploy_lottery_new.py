from __future__ import annotations
from scripts.helpful_scripts import get_account, get_contract, fund_with_link
from brownie import Lottery, network, config
import time
from abc import ABC, abstractmethod

class Options(ABC):
    @abstractmethod
    def start_lottery(self):
        ...
    
    @abstracmethod
    def enter_lottery(self):
        ...
    
    @abtractmethod
    def end_lottery(self):
        ...

class Deploy(Options):
    def __init__(self):
        self.account = get_account()
        self.lottery = Lottery.deploy(
            get_contract('eth_usd_price_feed').address,
            get_contract('vrf_coordinator').address,
            get_contract('link_token').address,
            config['networks'][network.show_active()]['fee'],
            config['networks'][network.show_active()]['keyhash'],
            {'from': account},
            publish_source = config['networks'][network.show_active()].get('verify', False)
        )
        self.get_deploy(self.lottery)

    def get_deploy(self, lottery):
        print('Deployed lottery!')
        return lottery

    def start_lottery(self):
        self.account_p = get_account()
        self.lottery_p = Lottery[-1]
        self.starting_txn = self.lottery_p.start_lottery({'from': self.account_p})
        self.starting_txn.wait(1)
        print('The lottery has started')
    
    def enter_lottery(self):
        self.account_x = get_account()
        self.lottery_x = Lottery[-1]
        self.value = self.lottery_x.getEntranceFee() + 100000000
        self.tx = self.lottery_x.enter({'from': self.account_x, 'value': self.value})
        self.tx.wait(1)
        print('You has entered to the lottery')
    
    def end_lottery(self):
        self.account_z = get_account()
        self.lottery_z = Lottery[-1]
        self.txn = fund_with_link(self.lottery_z.address)
        self.txn.wait(1)
        self.ending_transaction = self.lottery_z.endLottery({'from': self.account_z})
        self.ending_transaction.wait(1)
        time.sleep(60)
        print(f'{self.lottery_z.recentWinner()} is the new winner !!!')

lottery = Deploy()

lottery.start_lottery()

lottery.enter_lottery()

lottery.end_lottery()