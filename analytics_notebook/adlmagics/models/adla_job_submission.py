class AdlaJobSubmission:
    def __init__(self, name, script, parallelism, priority, runtime):
        self.name = name
        self.script = script
        self.parallelism = parallelism
        self.priority = priority
        self.runtime = runtime