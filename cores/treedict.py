from collections import OrderedDict


################################################################################
### TreeDict-key sorted dict
################################################################################
class TreeDict(OrderedDict):
    def __init__(self, arr, reverse=False):
        self._reverse = reverse
        super(TreeDict, self).__init__(sorted(arr, reverse=reverse))

    # put key,value and re-sort
    def put_in_order(self, key, value, dict_setitem=dict.__setitem__):
        root = self._OrderedDict__root
        first = root[1]
        last = root[0]
        if key not in self:
            if not self._reverse:
                if key < first[2]:
                    first[0] = root[1] = self._OrderedDict__map[key] = [root, first, key]
                elif key > last[2]:
                    last[1] = root[0] = self._OrderedDict__map[key] = [last, root, key]
                else:
                    while key > first[2]:
                        first = first[1]
                    prev_ = first[0]
                    next_ = first
                    prev_[1] = next_[0] = self._OrderedDict__map[key] = [prev_, next_, key]
            else:
                if key > first[2]:
                    first[0] = root[1] = self._OrderedDict__map[key] = [root, first, key]
                elif key < last[2]:
                    last[1] = root[0] = self._OrderedDict__map[key] = [last, root, key]
                else:
                    while key < first[2]:
                        first = first[1]
                    prev_ = first[0]
                    next_ = first
                    prev_[1] = next_[0] = self._OrderedDict__map[key] = [prev_, next_, key]
        return dict_setitem(self, key, value)

    def get_first(self):
        key = next(iter(self))
        value = self.get(key)
        return key, value
