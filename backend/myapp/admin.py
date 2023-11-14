from django.contrib import admin
from .models import Incident
from .forms import IncidentForm

from django.utils.html import format_html

class IncidentAdmin(admin.ModelAdmin):
    #radio_fields={"Type_of_near_miss": admin.HORIZONTAL,"Safety_violated": admin.HORIZONTAL}
    form=IncidentForm
    list_filter =['situation']
    list_display=['name','Witnesses','Departments','Location_Area','Incident_report_date','Type_of_near_miss','Description','Safety_violated','Recommendation_step','status','_']
    search_fields=['name','Witnesses','Departments','Location_Area','Incident_report_date','Type_of_near_miss','Description','Safety_violated','Recommendation_step','situation']
    list_per_page=10

    # Function to change the icons
    def _(self, obj):
        if obj.situation =='Approved':
            return True
        elif obj.situation == 'Pending':
            return None
        else:
            return False
    _.boolean = True

    #Function to color the text
    def status(self, obj):
        if obj.situation =='Approved':
            color = '#28a745'
        elif obj.situation == 'Pending':
           color ='#fea95e'
        else:
            color ='red'
        return format_html('<strong><p style="color:{}">{}</p></strong>'.format(color,obj.situation))
    status.allow_tags = True

admin.site.register(Incident,IncidentAdmin)
