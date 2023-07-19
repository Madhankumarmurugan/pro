from django.shortcuts import render
import datetime
import random

# Create your views here.
def result_view(request):
    msg=[
        'The Golden days is ahead',
        'Today is the best life of day',
        'Very soon your going to get job',
        'Today Your are going to extra expenses, so be closed your hand',
        'May You Will get new friend or person and your life is going to change'
        ]
    comp_list=[
        'infosis',
        'Wipro',
        'polaries',
        'UST Golbal',
        'TCS',
        'CTS'
    ]
    dt=datetime.datetime.now()
    h=int(dt.strftime('%H'))
    if h<12:
        s='good morning friend'
    elif h<16:
        s='good afternoon friend'
    elif h<21:
        s='good evening friend'
    else:
        s='good night friend'
    cName=random.choice(comp_list)
    amsg=random.choice(msg)  
    my_data={
        'dt':dt,
        'wishmsg':s,
        'cname':cName,
        'ast_msg':amsg
}
    return render(request,'html/mk.html',context=my_data)                  