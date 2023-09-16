#_*_ encoding: utf-8 *_*
from django import forms
from . import models
from captcha.fields import CaptchaField

class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):

        super(ContactForm, self).__init__(*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


    CITY = [
        ['TP', 'Taipei'],
        ['TY', 'Taoyuang'],
        ['TC', 'Taichung'],
        ['TN', 'Tainan'],
        ['KS', 'Kaohsiung'],
        ['NA', 'Others'],
        ]

    # form = forms.ContactForm(request.POST)
    # if form.is_valid():
    #     message = "感謝您的來信。"
    #     user_name = form.cleaned_data['user_name']
    #     user_city = form.cleaned_data['user_city']
    #     user_school = form.cleaned_data['user_school']
    #     user_email = form.cleaned_data['user_email']
    #     user_message = form.cleaned_data['user_message']
    # else:
    #     message = "請檢查您輸入的資訊是否正確！"

    user_name = forms.CharField(label='您的姓名', max_length=50, initial='NA')
    user_city = forms.ChoiceField(label='居住城市', choices=CITY)
    user_school = forms.BooleanField(label='是否在學', required=False)
    user_email = forms.EmailField(label='電子郵件')
    user_message = forms.CharField(label='您的意見', widget=forms.Textarea)


class PostForm(forms.ModelForm):
    #captcha = CaptchaField()
    class Meta:
        model = models.Post
        fields = ['mood', 'nickname', 'message', 'del_pass']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['mood'].label = '現在心情'
        self.fields['nickname'].label = '你的暱稱'
        self.fields['message'].label = '心情留言'
        self.fields['del_pass'].label = '設定密碼'
        #self.fields['captcha'].label = '驗證碼'

class LoginForm(forms.Form):
    username = forms.CharField(label='姓名', max_length=10)
    password = forms.CharField(label='密碼',widget=forms.PasswordInput())

class DateInput(forms.DateInput):
    input_type = 'date'

class DiaryForm(forms.ModelForm):
    class Meta:
        model = models.Diary
        fields = ['budget', 'weight', 'note', 'ddate']
        widgets = {'ddate': DateInput(),}

        def __init__(self, *args, **kwargs):
            super(DiaryForm, self).__init__(*args, **kwargs)
            #self.fields['user'].label = 'User'
            self.fields['budget'].label = '今日花費(元)'
            self.fields['weight'].label = '今日體重(KG)'
            self.fields['note'].label = '心情留言'
            self.fields['ddate'].label = '日期'