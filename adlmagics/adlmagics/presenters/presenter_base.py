class PresenterBase:
    def is_presentable(self, obj):
        pass
    
    def present(self, obj):
        if not self.is_presentable(obj):
            raise ValueError("Type '%s' is not presentable by '%s'" % (type(obj).__name__, PresenterBase.__name__))