from django import forms
from .models import Appointment, TakeAppointment


class CreateAppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].label = "Полное ФИО"
        self.fields['image'].label = "Фото"
        self.fields['department'].label = "Гос Структура"
        self.fields['start_time'].label = "Начало"
        self.fields['hospital_name'].label = "Название"
        self.fields['qualification_name'].label = "Просьбы"
        self.fields['institute_name'].label = "Цель"

        self.fields['full_name'].widget.attrs.update(
            {
                'placeholder': 'ФИО',
            }
        )

        self.fields['department'].widget.attrs.update(
            {
                'placeholder': 'Услуги',
            }
        )

        self.fields['start_time'].widget.attrs.update(
            {
                'placeholder': '9:00',
            }
        )
        self.fields['end_time'].widget.attrs.update(
            {
                'placeholder': '12:00',
            }
        )
        self.fields['location'].widget.attrs.update(
            {
                'placeholder': 'Аддрес',
            }
        )

        self.fields['hospital_name'].widget.attrs.update(
            {
                'placeholder': 'Название',
            }
        )

        self.fields['qualification_name'].widget.attrs.update(
            {
                'placeholder': 'Улучшить Парк',
            }
        )

        self.fields['institute_name'].widget.attrs.update(
            {
                'placeholder': 'Сделать Реставрацию Парка',
            }
        )

    class Meta:
        model = Appointment
        fields = ['full_name', 'image', 'department', 'start_time', 'end_time', 'location',
                  'hospital_name', 'qualification_name', 'institute_name']

    def is_valid(self):
        valid = super(CreateAppointmentForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        appointment = super(CreateAppointmentForm, self).save(commit=False)
        if commit:
            appointment.save()
        return appointment


class TakeAppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TakeAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['appointment'].label = "Выберите Услуги"
        self.fields['full_name'].label = "Фио"
        self.fields['phone_number'].label = "Номер Телефона"
        self.fields['message'].label = "Описание Проблемы"

        self.fields['appointment'].widget.attrs.update(
            {
                'placeholder': 'Услуги',
            }
        )

        self.fields['full_name'].widget.attrs.update(
            {
                'placeholder': 'ФИО',
            }
        )

        self.fields['phone_number'].widget.attrs.update(
            {
                'placeholder': 'Номер Телефона',
            }
        )
        self.fields['message'].widget.attrs.update(
            {
                'placeholder': 'Описание    ',
            }
        )

    class Meta:
        model = TakeAppointment
        fields = ['appointment', 'full_name', 'phone_number', 'message']

    def is_valid(self):
        valid = super(TakeAppointmentForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        appointment = super(TakeAppointmentForm, self).save(commit=False)
        if commit:
            appointment.save()
        return appointment
