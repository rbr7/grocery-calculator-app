from django import forms

class SignupForm(forms.Form):
    username= forms.CharField(max_length=20)
    password=forms.CharField(widget=forms.PasswordInput())
    emailid=forms.CharField(max_length=30)
    phoneno=forms.CharField(max_length=15)

    def clean_message(self):
        username=self.cleaned_data.get("username")
        emailid = self.cleaned_data.get("emailid")
        phoneno = self.cleaned_data.get("phoneno")
        password= self.cleaned_data.get("password")
        return(username,emailid,phoneno,password)

class LoginForm(forms.Form):
    emailid=forms.CharField(max_length=30)
    password=forms.CharField(widget=forms.PasswordInput())


    def clean_message(self):
        emailid=self.cleaned_data.get("emailid")
        password=self.cleaned_data.get("password")
        return(emailid,password)

class AddgForm(forms.Form):
    coffee =forms.BooleanField(required=False)
    quantityc=forms.IntegerField(required=False)
    uqc=forms.CharField()
    wcc= forms.IntegerField(required=False)
    uwc=forms.CharField()

    rice = forms.BooleanField(required=False)
    quantityr = forms.IntegerField(required=False)
    uqr = forms.CharField()
    wcr = forms.IntegerField(required=False)
    uwr = forms.CharField()

    sugar = forms.BooleanField(required=False)
    quantitys = forms.IntegerField(required=False)
    uqs = forms.CharField()
    wcs = forms.IntegerField(required=False)
    uws = forms.CharField()

    pulses = forms.BooleanField(required=False)
    quantityp = forms.IntegerField(required=False)
    uqp = forms.CharField()
    wcp = forms.IntegerField(required=False)
    uwp = forms.CharField()

    def clean_message(self):
        coffee= self.cleaned_data.get('coffee')
        quantityc= self.cleaned_data.get('quantityc')
        uqc= self.cleaned_data.get('uqc')
        wcc= self.cleaned_data.get('wcc')
        uwc=self.cleaned_data.get('uwc')
        dc ={'coffee':[coffee,quantityc,uqc,wcc,uwc]}

        rice = self.cleaned_data.get('rice')
        quantityr = self.cleaned_data.get('quantityr')
        uqr = self.cleaned_data.get('uqr')
        wcr = self.cleaned_data.get('wcr')
        uwr = self.cleaned_data.get('uwr')
        dr = {'rice': [rice, quantityr, uqr, wcr, uwr]}

        sugar = self.cleaned_data.get('sugar')
        quantitys = self.cleaned_data.get('quantitys')
        uqs = self.cleaned_data.get('uqs')
        wcs = self.cleaned_data.get('wcs')
        uws = self.cleaned_data.get('uws')
        ds = {'sugar': [sugar, quantitys, uqs, wcs, uws]}

        pulses = self.cleaned_data.get('pulses')
        quantityp = self.cleaned_data.get('quantityp')
        uqp = self.cleaned_data.get('uqp')
        wcp = self.cleaned_data.get('wcp')
        uwp = self.cleaned_data.get('uwp')
        dp = {'pulses': [pulses, quantityp, uqp, wcp, uwp]}
        print  (coffee,quantityc,uqc,wcc,uwc)
        return (dc,dr,ds,dp)


class AddgOwnForm(forms.Form):
    g1 =forms.CharField(max_length=15,required=False)
    q1=forms.IntegerField(required=False)
    uq1=forms.CharField()
    wc1= forms.IntegerField(required=False)
    uw1=forms.CharField()

    g2 = forms.CharField(max_length=15, required=False)
    q2 = forms.IntegerField(required=False)
    uq2 = forms.CharField()
    wc2 = forms.IntegerField(required=False)
    uw2 = forms.CharField()

    g3 =forms.CharField(max_length=15,required=False)
    q3=forms.IntegerField(required=False)
    uq3=forms.CharField()
    wc3= forms.IntegerField(required=False)
    uw3=forms.CharField()

    def clean_message(self):
        g1= self.cleaned_data.get('g1')
        q1= self.cleaned_data.get('q1')
        uq1= self.cleaned_data.get('uq1')
        wc1= self.cleaned_data.get('wc1')
        uw1=self.cleaned_data.get('uw1')
        dg1 ={'g1':[g1,q1,uq1,wc1,uw1]}

        g2 = self.cleaned_data.get('g2')
        q2 = self.cleaned_data.get('q2')
        uq2 = self.cleaned_data.get('uq2')
        wc2 = self.cleaned_data.get('wc2')
        uw2 = self.cleaned_data.get('uw2')
        dg2 = {'g2': [g2, q2, uq2, wc2, uw2]}

        g3= self.cleaned_data.get('g3')
        q3= self.cleaned_data.get('q3')
        uq3= self.cleaned_data.get('uq3')
        wc3= self.cleaned_data.get('wc3')
        uw3=self.cleaned_data.get('uw3')
        dg3 ={'g3':[g3,q3,uq3,wc3,uw3]}

        return (dg1 ,dg2, dg3)


