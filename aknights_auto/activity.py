import pyautogui

from aknights_auto.constant import MenuLevelConstant

class Activity(object):

    def __init__(self,add_san_times=0, use_stone=False):
        self._cur_status = MenuLevelConstant.main_menu
        self._time_lag = 1
        self._compelet_times = 0
        self._add_san_times = add_san_times
        self._use_stone = use_stone
        pass

    def start_activity(self):
        pass
        self._compelet_times = self._compelet_times + 1
        # todo 升级应对

    def add_san(self):
        pass

    def find_way(self, input):

        if (input):
            self._cur_status = MenuLevelConstant.main_menu
        pass


