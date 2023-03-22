from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class ToDo(models.Model):
    number = models.CharField('Номер телефона', max_length=50, blank=True, null=True)
    site = models.CharField('Сайт', max_length=50, blank=True, null=True)
    datatime = models.DateField('Следующий звонок', auto_now = False , auto_now_add = False)
    comment = models.TextField('Комментарий',max_length = 1000)
    is_complete = models.BooleanField('Завершено', default=False)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.number
    


class Comment(models.Model):
    number = models.ForeignKey(ToDo,
                             on_delete=models.CASCADE,
                             related_name='comments',
                             verbose_name='Задача',
                             blank=True,
                             null=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name='Автор')
    text = models.TextField('Комментарий', help_text='Напишите комментарий')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'