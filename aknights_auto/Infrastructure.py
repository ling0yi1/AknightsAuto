from aknights_auto.constant import MenuLevelConstant


class Infrastructure(object):

    def __init__(self):
        self._cur_status = MenuLevelConstant.main_menu
        self._time_lag = 1

    def auto_run(self):
        pass

    def run_trading_station(self):
        pass

    def run_manufactruring_station(self):
        pass

    def run_power_station(self):
        pass

    def run_dormitory(self):
        pass

    def run_meeting_room(self):
        pass

    def run_office(self):
        pass
