from typing import List

from .constants import CUT_OFF_PERCENTAGE
from .definitions import Bent, Cap, Group
from .goals import Regions, Sectors


class Symbol:
    def __init__(self, ticker: str, cap: str, gbv: str, bonds: float, sectors: List[float], regions: List[float]):
        self.ticker = ticker
        self.cap = Cap[cap]
        self.bent = Bent[gbv]
        self.bond_percentage = bonds
        self.sector_weights = Sectors(*sectors)
        self.regional_distribution = Regions(*regions)
    
    @property
    def is_alternative(self):
        return self.sector_weights.Real_Estate >= CUT_OFF_PERCENTAGE
    
    @property
    def is_bond(self):
        return self.bond_percentage >= CUT_OFF_PERCENTAGE
    
    @property
    def is_domestic(self):
        return self.regional_distribution.United_States >= CUT_OFF_PERCENTAGE
    
    @property
    def grouping(self):
        if self.is_alternative:
            return Group['Alternatives']
        if self.is_bond:
            return Group['USA_Bonds'] if self.is_domestic else Group['Intl_Bonds']
        else:
            return Group['USA_Stocks'] if self.is_domestic else Group['Intl_Stocks']
