
class ObserveValue:
    def __init__(self, initial_value=0):
        self._value = initial_value
        self._callbacks = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        old_value = self._value
        self._value = new_value
        self._notify(old_value, new_value)
    
    def _notify(self, old_val, new_val):
        for cb in self._callbacks:
            cb(old_val,new_val)

    def reg_cb(self, callback):
        self._callbacks.append(callback)

if __name__ == "__main__":
    def print_if_change_greater_than_500(old_value, new_value):
        if abs(old_value - new_value) > 500:
            print(f'The value changed by more than 500 (from {old_value} to {new_value})')

    holder = ObserveValue()
    holder.reg_cb(print_if_change_greater_than_500)
    holder.value = 7    # nothing is printed
    holder.value = 70   # nothing is printed
    holder.value = 700  # a message is printed    

