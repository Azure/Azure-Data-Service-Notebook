class MockResultReceiver:
    def __init__(self):
        self.__last_received_result_name = None
        self.__last_received_result_value = None

    def receive(self, result_name, result_value):
        self.__last_received_result_name = result_name
        self.__last_received_result_value = result_value

    @property
    def last_received_result_name(self):
        return self.__last_received_result_name

    @property
    def last_received_result_value(self):
        return self.__last_received_result_value