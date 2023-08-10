CON_SLOT_NONE = 'IS_NONE'
CON_SLOT_NOT_EXISTING = 'IS_NOT_EXISTING'
CON_SLOT_EXISTING = 'IS_EXISTING'

class SlotIdentification:
    def __init__(self):
        self.message = None
        self.name = None
        
    @staticmethod
    def builder(name):
        instance = SlotIdentification()
        instance.name = name
        return instance

    def check_none(self):
        if self.name is None and self.message is None:
            self.message = CON_SLOT_NONE
        return self
    
    def check_existing(self, slot_exist):
        if self.name not in slot_exist and self.message is None:
            self.message = CON_SLOT_NOT_EXISTING
        return self

    def build(self):
        if self.message is None:
            self.message = CON_SLOT_EXISTING
        return self.message
    

