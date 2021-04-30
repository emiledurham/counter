from django.shortcuts import render
from .models import T1, T2, QC
from .forms import T1Form, T2Form, QCForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import operator
import plotly.graph_objs as go
import os
import datetime
from datetime import date
import numpy as np


# Create your views here.

@login_required(login_url="/accounts/login")
def home(request):

    single_date_count_t1 = len(T1.objects.filter(date__startswith=date.today()))
    single_date_count_t2 = len(T2.objects.filter(date__startswith=date.today()))
    single_date_count_qc = len(QC.objects.filter(date__startswith=date.today()))
    single_date_count_t2_2 = single_date_count_t2*2
    single_date_sum = single_date_count_t1 + single_date_count_t2_2 + single_date_count_qc
    today = datetime.datetime.today()

    return render(request, 'home.html', {'single_date_count_t1': single_date_count_t1,
                                         'single_date_count_t2': single_date_count_t2,
                                         'single_date_count_qc': single_date_count_qc,
                                         'single_date_count_t2_2': single_date_count_t2_2,
                                         'single_date_sum': single_date_sum,
                                         'today': today})


def add_t1(request):
    if request.method == 'POST':
        form1 = T1Form(request.POST or None)
        if form1.is_valid():
            form1.save()

        single_date_count_t1 = len(T1.objects.filter(date__startswith=date.today()))
        single_date_count_t2 = len(T2.objects.filter(date__startswith=date.today()))
        single_date_count_qc = len(QC.objects.filter(date__startswith=date.today()))
        single_date_count_t2_2 = single_date_count_t2 * 2
        single_date_sum = single_date_count_t1 + single_date_count_t2_2 + single_date_count_qc
        today = datetime.datetime.today()

        return render(request, 'home.html', {'single_date_count_t1': single_date_count_t1,
                                             'single_date_count_t2': single_date_count_t2,
                                             'single_date_count_qc': single_date_count_qc,
                                             'single_date_count_t2_2': single_date_count_t2_2,
                                             'single_date_sum': single_date_sum,
                                             'today': today})

    single_date_count_t1 = len(T1.objects.filter(date__startswith=date.today()))
    single_date_count_t2 = len(T2.objects.filter(date__startswith=date.today()))
    single_date_count_qc = len(QC.objects.filter(date__startswith=date.today()))
    single_date_count_t2_2 = single_date_count_t2 * 2
    single_date_sum = single_date_count_t1 + single_date_count_t2_2 + single_date_count_qc
    today = datetime.datetime.today()

    return render(request, 'home.html', {'single_date_count_t1': single_date_count_t1,
                                         'single_date_count_t2': single_date_count_t2,
                                         'single_date_count_qc': single_date_count_qc,
                                         'single_date_count_t2_2': single_date_count_t2_2,
                                         'single_date_sum': single_date_sum,
                                         'today': today})


def add_t2(request):
    if request.method == 'POST':
        form2 = T2Form(request.POST or None)
        if form2.is_valid():
            form2.save()

            single_date_count_t1 = len(T1.objects.filter(date__startswith=date.today()))
            single_date_count_t2 = len(T2.objects.filter(date__startswith=date.today()))
            single_date_count_qc = len(QC.objects.filter(date__startswith=date.today()))
            single_date_count_t2_2 = single_date_count_t2 * 2
            single_date_sum = single_date_count_t1 + single_date_count_t2_2 + single_date_count_qc
            today = datetime.datetime.today()

            return render(request, 'home.html', {'single_date_count_t1': single_date_count_t1,
                                                 'single_date_count_t2': single_date_count_t2,
                                                 'single_date_count_qc': single_date_count_qc,
                                                 'single_date_count_t2_2': single_date_count_t2_2,
                                                 'single_date_sum': single_date_sum,
                                                 'today': today})

        single_date_count_t1 = len(T1.objects.filter(date__startswith=date.today()))
        single_date_count_t2 = len(T2.objects.filter(date__startswith=date.today()))
        single_date_count_qc = len(QC.objects.filter(date__startswith=date.today()))
        single_date_count_t2_2 = single_date_count_t2 * 2
        single_date_sum = single_date_count_t1 + single_date_count_t2_2 + single_date_count_qc
        today = datetime.datetime.today()

        return render(request, 'home.html', {'single_date_count_t1': single_date_count_t1,
                                             'single_date_count_t2': single_date_count_t2,
                                             'single_date_count_qc': single_date_count_qc,
                                             'single_date_count_t2_2': single_date_count_t2_2,
                                             'single_date_sum': single_date_sum,
                                             'today': today})


def add_qc(request):
    if request.method == 'POST':
        form3 = QCForm(request.POST or None)
        if form3.is_valid():
            form3.save()

            single_date_count_t1 = len(T1.objects.filter(date__startswith=date.today()))
            single_date_count_t2 = len(T2.objects.filter(date__startswith=date.today()))
            single_date_count_qc = len(QC.objects.filter(date__startswith=date.today()))
            single_date_count_t2_2 = single_date_count_t2 * 2
            single_date_sum = single_date_count_t1 + single_date_count_t2_2 + single_date_count_qc
            today = datetime.datetime.today()

            return render(request, 'home.html', {'single_date_count_t1': single_date_count_t1,
                                                 'single_date_count_t2': single_date_count_t2,
                                                 'single_date_count_qc': single_date_count_qc,
                                                 'single_date_count_t2_2': single_date_count_t2_2,
                                                 'single_date_sum': single_date_sum,
                                                 'today': today})

        single_date_count_t1 = len(T1.objects.filter(date__startswith=date.today()))
        single_date_count_t2 = len(T2.objects.filter(date__startswith=date.today()))
        single_date_count_qc = len(QC.objects.filter(date__startswith=date.today()))
        single_date_count_t2_2 = single_date_count_t2 * 2
        single_date_sum = single_date_count_t1 + single_date_count_t2_2 + single_date_count_qc
        today = datetime.datetime.today()

        return render(request, 'home.html', {'single_date_count_t1': single_date_count_t1,
                                             'single_date_count_t2': single_date_count_t2,
                                             'single_date_count_qc': single_date_count_qc,
                                             'single_date_count_t2_2': single_date_count_t2_2,
                                             'single_date_sum': single_date_sum,
                                             'today': today})


def delete_t1(request):
    try:
        x = T1.objects.filter(date__startswith=date.today()).last()
        x.delete()

        single_date_count_t1 = len(T1.objects.filter(date__startswith=date.today()))
        single_date_count_t2 = len(T2.objects.filter(date__startswith=date.today()))
        single_date_count_qc = len(QC.objects.filter(date__startswith=date.today()))
        single_date_count_t2_2 = single_date_count_t2 * 2
        single_date_sum = single_date_count_t1 + single_date_count_t2_2 + single_date_count_qc
        today = datetime.datetime.today()

        return render(request, 'home.html', {'single_date_count_t1': single_date_count_t1,
                                             'single_date_count_t2': single_date_count_t2,
                                             'single_date_count_qc': single_date_count_qc,
                                             'single_date_count_t2_2': single_date_count_t2_2,
                                             'single_date_sum': single_date_sum,
                                             'today': today})


    except Exception as e:
        single_date_count_t1 = "error"

        single_date_count_t1 = len(T1.objects.filter(date__startswith=date.today()))
        single_date_count_t2 = len(T2.objects.filter(date__startswith=date.today()))
        single_date_count_qc = len(QC.objects.filter(date__startswith=date.today()))
        single_date_count_t2_2 = single_date_count_t2 * 2
        single_date_sum = single_date_count_t1 + single_date_count_t2_2 + single_date_count_qc
        today = datetime.datetime.today()

        return render(request, 'home.html', {'single_date_count_t1': single_date_count_t1,
                                             'single_date_count_t2': single_date_count_t2,
                                             'single_date_count_qc': single_date_count_qc,
                                             'single_date_count_t2_2': single_date_count_t2_2,
                                             'single_date_sum': single_date_sum,
                                             'today': today})


def delete_t2(request):
    try:
        x = T2.objects.filter(date__startswith=date.today()).last()
        x.delete()

        single_date_count_t1 = len(T1.objects.filter(date__startswith=date.today()))
        single_date_count_t2 = len(T2.objects.filter(date__startswith=date.today()))
        single_date_count_qc = len(QC.objects.filter(date__startswith=date.today()))
        single_date_count_t2_2 = single_date_count_t2 * 2
        single_date_sum = single_date_count_t1 + single_date_count_t2_2 + single_date_count_qc
        today = datetime.datetime.today()

        return render(request, 'home.html', {'single_date_count_t1': single_date_count_t1,
                                             'single_date_count_t2': single_date_count_t2,
                                             'single_date_count_qc': single_date_count_qc,
                                             'single_date_count_t2_2': single_date_count_t2_2,
                                             'single_date_sum': single_date_sum,
                                             'today': today})


    except Exception as e:
        single_date_count_t1 = "error"

        single_date_count_t1 = len(T1.objects.filter(date__startswith=date.today()))
        single_date_count_t2 = len(T2.objects.filter(date__startswith=date.today()))
        single_date_count_qc = len(QC.objects.filter(date__startswith=date.today()))
        single_date_count_t2_2 = single_date_count_t2 * 2
        single_date_sum = single_date_count_t1 + single_date_count_t2_2 + single_date_count_qc
        today = datetime.datetime.today()

        return render(request, 'home.html', {'single_date_count_t1': single_date_count_t1,
                                             'single_date_count_t2': single_date_count_t2,
                                             'single_date_count_qc': single_date_count_qc,
                                             'single_date_count_t2_2': single_date_count_t2_2,
                                             'single_date_sum': single_date_sum,
                                             'today': today})


def delete_qc(request):
    try:
        x = QC.objects.filter(date__startswith=date.today()).last()
        x.delete()

        single_date_count_t1 = len(T1.objects.filter(date__startswith=date.today()))
        single_date_count_t2 = len(T2.objects.filter(date__startswith=date.today()))
        single_date_count_qc = len(QC.objects.filter(date__startswith=date.today()))
        single_date_count_t2_2 = single_date_count_t2 * 2
        single_date_sum = single_date_count_t1 + single_date_count_t2_2 + single_date_count_qc
        today = datetime.datetime.today()

        return render(request, 'home.html', {'single_date_count_t1': single_date_count_t1,
                                             'single_date_count_t2': single_date_count_t2,
                                             'single_date_count_qc': single_date_count_qc,
                                             'single_date_count_t2_2': single_date_count_t2_2,
                                             'single_date_sum': single_date_sum,
                                             'today': today})


    except Exception as e:
        single_date_count_t1 = "error"

        single_date_count_t1 = len(T1.objects.filter(date__startswith=date.today()))
        single_date_count_t2 = len(T2.objects.filter(date__startswith=date.today()))
        single_date_count_qc = len(QC.objects.filter(date__startswith=date.today()))
        single_date_count_t2_2 = single_date_count_t2 * 2
        single_date_sum = single_date_count_t1 + single_date_count_t2_2 + single_date_count_qc
        today = datetime.datetime.today()

        return render(request, 'home.html', {'single_date_count_t1': single_date_count_t1,
                                             'single_date_count_t2': single_date_count_t2,
                                             'single_date_count_qc': single_date_count_qc,
                                             'single_date_count_t2_2': single_date_count_t2_2,
                                             'single_date_sum': single_date_sum,
                                             'today': today})


@login_required(login_url='/accounts/login')
def dashboard(request):
    try:
        os.chdir('word_counter_app/templates')
    except:
        pass

    id_list = 0
    date_list = []
    for item in T1.objects.values():
        if item['id']:
            id_list += 1
        date_list.append(item['date'])

    id_list2 = 0
    date_list2 = []
    for item2 in T2.objects.values():
        if item2['id']:
            id_list2 += 1
        date_list2.append(item2['date'])

    id_list3 = 0
    date_list3 = []
    for item3 in QC.objects.values():
        if item3['id']:
            id_list3 += 1
        date_list3.append(item3['date'])

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[i for i in date_list], y=[i for i in range(id_list)], name='T1'))
    fig.add_trace(go.Scatter(x=[i for i in date_list2], y=[i for i in range(id_list2)], name='T2'))
    fig.add_trace(go.Scatter(x=[i for i in date_list3], y=[i for i in range(id_list3)], name='QC'))
    fig.update_layout(yaxis=dict(range=[0, [i for i in range(id_list)]]),
                      xaxis=dict(range=[date.today(), [i.date() for i in date_list]]),
                      )
    fig.write_html('graph.html')
    graph = fig.to_html()

    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x=[i.date() for i in date_list], y=[len(date_list)], text=[len(date_list)], textposition='auto', name='T1'))
    fig2.add_trace(go.Bar(x=[i.date() for i in date_list2], y=[len(date_list2)], text=[len(date_list2)], textposition='auto', name='T2'))
    fig2.add_trace(go.Bar(x=[i.date() for i in date_list3], y=[len(date_list3)], text=[len(date_list3)], textposition='auto', name='QC'))
    fig2.write_html('graph2.html')
    graph2 = fig2.to_html()

    fig3 = go.Figure()
    fig3.add_trace(go.Pie(labels=['T1','T2', 'QC'], values=[len(date_list),len(date_list2), len(date_list3)], textposition='auto'))
    fig3.write_html('graph3.html')
    graph3 = fig3.to_html()

    date_count_t1 = len(T1.objects.all())
    date_count_t2 = len(T2.objects.all())
    date_count_qc = len(QC.objects.all())
    single_date_count_t1 = len(T1.objects.filter(date__startswith=date.today()))
    single_date_count_t2 = len(T2.objects.filter(date__startswith=date.today()))
    single_date_count_qc = len(QC.objects.filter(date__startswith=date.today()))
    single_date_count_t2_2 = single_date_count_t2 * 2
    single_date_sum = single_date_count_t1 + single_date_count_t2_2 + single_date_count_qc
    today = datetime.datetime.today()

    return render(request, 'dashboard.html', {'single_date_count_t1': single_date_count_t1,
                                              'single_date_count_t2': single_date_count_t2,
                                              'single_date_count_qc': single_date_count_qc,
                                              'single_date_count_t2_2': single_date_count_t2_2,
                                              'single_date_sum': single_date_sum,
                                              'today': today,
                                              'graph': graph,
                                              'graph2': graph2,
                                              'graph3': graph3,
                                              'date_count_t1': date_count_t1,
                                              'date_count_t2': date_count_t2,
                                              'date_count_qc': date_count_qc})


def counter(request):
    if request.method == 'POST':
        data = request.POST['data']
        data_list = data.split()
        word_dict = {}
        for word in data_list:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
        sorted_words = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)

        return render(request, 'counter.html', {'data_list': len(data_list), 'word_dict': sorted_words})
    return render(request, 'counter.html')




