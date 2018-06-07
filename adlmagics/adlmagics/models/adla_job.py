class AdlaJob:
    def __init__(self, id, name, type, submitter, parallelism, priority, submit_time, start_time, end_time, state, result):
        self.id = id
        self.name = name
        self.type = type
        self.submitter = submitter
        self.parallelism = parallelism
        self.priority = priority
        self.submit_time = submit_time
        self.start_time = start_time
        self.end_time = end_time
        self.state = state
        self.result = result