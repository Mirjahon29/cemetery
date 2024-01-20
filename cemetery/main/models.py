from django.db import models

class employee(models.Model):
    surname=models.CharField(max_length=50,verbose_name='Фамилия сотрудника')
    name=models.CharField(max_length=50,verbose_name='Имя сотрудника')
    middlename=models.CharField(max_length=50,verbose_name='Отчество сотрудника')    
    birth=models.DateField(verbose_name='Дата рождения')
    snils=models.CharField(max_length=50,verbose_name='СНИЛС')
    inn=models.CharField(max_length=50,verbose_name='ИНН')
    def __str__(self):
        return self.surname
    class Meta:
        verbose_name_plural = 'Сотрудники кладбища'
        verbose_name = 'Сотрудник кладбища'
       
class area(models.Model):
    number=models.CharField(max_length=50,verbose_name='Номер участка')
    title=models.CharField(max_length=50,verbose_name='Название участка')
    employee_support=models.ForeignKey(employee,on_delete = models.CASCADE,verbose_name='Обслуживающий сотрудник',null=True,blank=True)
    def __str__(self):
        return self.number
    class Meta:
        verbose_name_plural = 'Участки'
        verbose_name = 'Участок'

class burial(models.Model):
    area_number=models.ForeignKey(area,on_delete = models.CASCADE,verbose_name='Участок',null=True,blank=True)
    number_burial=models.CharField(max_length=50,verbose_name='Номер захоронения на участке')
    surname_person=models.CharField(max_length=50,verbose_name='Фамилия захороненного')
    name_person=models.CharField(max_length=50,verbose_name='Имя захороненного')
    middlename_person=models.CharField(max_length=50,verbose_name='Отчество захороненного')  
    birth_person=models.DateField(verbose_name='Дата рождения захороненного')
    death_person=models.DateField(verbose_name='Дата смерти захороненного')
    def __str__(self):
        return self.number_burial
    class Meta:
        verbose_name_plural = 'Захоронения'
        verbose_name = 'Захоронение'