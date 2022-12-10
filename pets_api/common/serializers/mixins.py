from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ParseError


class ParseContextSerializerMixin(ModelSerializer):
    def _get_context_kwarg(self, context_field: str):
        """
            context_field - название поля в контексте \n
        """
        return self.context['request'].parser_context['kwargs'].get(
            context_field
        )

    def _get_obj_from_context(self,
                              context_field: str,
                              context_model,
                              context_model_field: str = 'id'):
        """
            context_field - название поля в контексте \n
            context_model - модель для получения обьекта
                            по данным из контекста \n
            context_model_field - поле для получения "context_model"
                                  по данным из контекста (по умол. id)
        """
        kwarg = self._get_context_kwarg(context_field)
        obj = context_model.objects.filter(
            **{context_model_field: kwarg}).first()
        if not obj:
            raise ParseError('The {} with {}="{}" was not found'.format(
                context_model.__name__,
                context_model_field,
                kwarg
            ))

        return obj
