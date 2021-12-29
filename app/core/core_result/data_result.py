class DataResult:
    def __init__(self,isSuccess:bool, message:str, data:object):
        self.isSuccess = isSuccess
        self.message = message
        self.data = data