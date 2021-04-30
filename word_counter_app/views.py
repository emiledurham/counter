from django.shortcuts import render
from django.db.models import Count
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
    date_count_t1 = len(T1.objects.all())
    date_count_t2 = len(T2.objects.all())
    date_count_qc = len(QC.objects.all())
    single_date_count_t1 = len(T1.objects.filter(date__startswith=date.today()))
    single_date_count_t2 = len(T2.objects.filter(date__startswith=date.today()))
    single_date_count_qc = len(QC.objects.filter(date__startswith=date.today()))
    single_date_count_t2_2 = single_date_count_t2 * 2
    single_date_sum = single_date_count_t1 + single_date_count_t2_2 + single_date_count_qc
    today = datetime.datetime.today()

    try:
        os.chdir('word_counter_app/templates')
    except:
        pass

    date_list_t1 = [item['date'] for item in T1.objects.values()]
    date_list_t2 = [item['date'] for item in T2.objects.values()]
    date_list_qc = [item['date'] for item in QC.objects.values()]

    id_list = [item['id'] for item in T1.objects.values()]
    id_list2 = [item['id'] for item in T2.objects.values()]
    id_list3 = [item['id'] for item in QC.objects.values()]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=date_list_t1, y=id_list, name='T1'))
    fig.add_trace(go.Scatter(x=date_list_t2, y=id_list2, name='T2'))
    fig.add_trace(go.Scatter(x=date_list_qc, y=id_list3, name='QC'))

    fig.write_html('graph.html')
    graph = fig.to_html()

    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x=[i.date() for i in date_list_t1], y=date_list_t1, text=[], textposition='auto', name='T1'))
    fig2.add_trace(go.Bar(x=[i.date() for i in date_list_t2], y=date_list_t2, text=[], textposition='auto', name='T2'))
    fig2.add_trace(go.Bar(x=[i.date() for i in date_list_qc], y=date_list_qc, text=[], textposition='auto', name='QC'))
    fig2.update_layout(yaxis=dict(range=[0, date_list_t1]),
                      xaxis=dict(range=[date.today(), date_list_t1]),
                      )

    fig2.write_html('graph2.html')
    graph2 = fig2.to_html()

    fig3 = go.Figure()
    fig3.add_trace(go.Pie(labels=['T1','T2', 'QC'], values=[len(date_list_t1),len(date_list_t2), len(date_list_qc)], textposition='auto'))
    fig3.write_html('graph3.html')
    graph3 = fig3.to_html()

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




