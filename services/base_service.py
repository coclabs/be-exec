class BaseService:
    def service(self, *args, **kwargs):
        raise NotImplementedError('Method service must be override by subclass.')
