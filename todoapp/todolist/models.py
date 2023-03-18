from django.db import models

class ToDo(models.Model):
    number = models.IntegerField('Номер телефона')
    site = models.CharField('Сайт', max_length=50, blank=True, null=True)
    datatime = models.DateTimeField('Следующий звонок', auto_now = False , auto_now_add = False)
    comment = models.TextField('Комментарий',max_length = 1000)
    is_complete = models.BooleanField('Завершено', default=False)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задания'

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)