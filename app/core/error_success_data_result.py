from app.core.core_result.data_result import DataResult


class ErrorDataResult(DataResult):
    def __init__(self, message=None, data=None):
        self.data = data
        super().__init__(isSuccess=False, message=message, data=data)
        
        
class SuccessDataResult(DataResult):
    def __init__(self, message= None, data = None):
        self.data = data
        super().__init__(isSuccess=True, message=message, data=data)
