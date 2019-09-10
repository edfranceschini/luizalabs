# coding=utf-8

class CustomModel:

    @property
    def serialize(self):
        fields = self._get_columns()
        rest = {}
        for field in fields:
            rest.__setitem__(field, self.__getattribute__(field))
        return rest

    # Só um teste para depois
    @property
    def created(self):
        return self.created.isoformat()


    def _get_columns(self):
        return self.__table__.columns.keys()

