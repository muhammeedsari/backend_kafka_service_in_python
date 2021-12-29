from app.core.core_result.result import Result

class SuccessResult(Result):
    def __init__(self, message):
        super().__init__(isSuccess=True, message=message)
        
        
class ErrorResult(Result):
    def __init__(self, message):
        super().__init__(isSuccess=False, message=message)
