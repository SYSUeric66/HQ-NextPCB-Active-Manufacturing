import abc

class FormPanelBase:
    def init(self) -> 'None':
        pass

    def is_valid(self) -> bool:
        return True
    
    @abc.abstractclassmethod
    def get_from(self) -> 'dict' :
        pass

    def on_region_changed(self):
        pass