from django import forms
from django.core.validators import RegexValidator
#from .models import SAFETY_VIOLATION,TYPE_NEAR_MISS

from .models import Incident


class IncidentForm(forms.ModelForm):

    #VALIDATIONS
    name = forms.CharField(
        label='Report By',min_length=3,max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',message="Only letters is allowed !")],
        widget=forms.TextInput(attrs={'placeholder':'Enter your name(optional)'}),
        required=False
        )
    
    Witnesses = forms.CharField(
        label='Witnesses',min_length=3,max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',message="Only letters is allowed !")],
        widget=forms.TextInput(attrs={'placeholder':'Enter the witness name'})
        )
    Departments = forms.CharField(
        label='Departments',min_length=3,max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',message="Only letters is allowed !")],
        widget=forms.TextInput(attrs={'placeholder':'Enter the department name where the near-miss or incident need to be report'})
        )
    
    Location_Area = forms.CharField(
        label='Location/Area',min_length=3,max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ-0-9\s]*$',message="Only letters or number is allowed !")],
        widget=forms.TextInput(attrs={'placeholder':'Enter the location/area where the near-miss or incident need to be report'})
        )
    
    Description = forms.CharField(
        label='Description',min_length=3,max_length=1000,
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ-0-9\s]*$',message="Only letters or number is allowed !")],
        widget=forms.Textarea(attrs={'placeholder':'If other selected, Describe the potential incident/hazard/concern and possible outcome (be detailed)','rows':5})
        )
    
    Recommendation_step = forms.CharField(
        label='Recommendations',min_length=3,max_length=1000,
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ-0-9\s]*$',message="Only letters or number is allowed !")],
        widget=forms.Textarea(attrs={'placeholder':'steps to take to prevent a similar incident.','rows':5})
        )
    
    class Meta:
        model = Incident
        #fields =['name','Witnesses','Departments','Location_Area','Type_of_near_miss','Description','Safety_violated','Recommendation_step','situation']
        exclude =['Incident_report_date','situation'] #if don't want to display this fiel on the screen
        #fields ="__all__"
        SAFETY_VIOLATION =[
                ('No','No'),
                ('Yes','Yes'),
                ('N/A','N/A'),
        ]

        TYPE_NEAR_MISS =[
                ('Safety Concern','Safety Concern'),
                ('Safety Idea/Suggestion','Safety Idea/Suggestion'),
                ('Near-Miss','Near-Miss'),
                ('Other','Other'),
        ]

        #OUTSIDE WIDGETS
        widgets ={
            'Safety_violated': forms.RadioSelect(
                choices=SAFETY_VIOLATION,
                attrs={
                    'class':'btn-check' # Bootstrap inside the forms.py
                }
            ),
            'Type_of_near_miss': forms.RadioSelect(
                choices=TYPE_NEAR_MISS,
                attrs={
                    'class':'btn-check' # Bootstrap inside the forms.py
                }
            ),
        }




   