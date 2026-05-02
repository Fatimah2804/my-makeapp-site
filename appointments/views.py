import random
from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import Appointment
from datetime import date, datetime, timedelta, time


def book_appointment(request):
    date_value = request.GET.get('date') or request.POST.get('date')
    time_value = request.GET.get('time') or request.POST.get('time')

    error = None

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():

            date_obj = datetime.strptime(date_value, '%Y-%m-%d').date()
            time_obj = datetime.strptime(time_value, '%H:%M').time()

            if Appointment.objects.filter(date=date_obj, time=time_obj).exists():
                error = "هذا الموعد محجوز بالفعل | התור כבר תפוס"
            else:
                appointment = form.save(commit=False)
                appointment.date = date_obj
                appointment.time = time_obj
                appointment.save()
                return redirect('success')
    else:
        form = AppointmentForm()

    return render(request, 'appointments/book_appointment.html', {
        'form': form,
        'date_value': date_value,
        'time_value': time_value,
        'error': error,
    })


def success_page(request):
    return render(request, 'appointments/success.html')


def weekly_schedule(request):
    selected_date_str = request.GET.get('selected_date')

    if selected_date_str:
        selected_date = datetime.strptime(selected_date_str, '%Y-%m-%d').date()
    else:
        selected_date = date.today()

    days_since_sunday = (selected_date.weekday() + 1) % 7
    start_of_week = selected_date - timedelta(days=days_since_sunday)

    week_days = []
    day_names = ['الأحد', 'الاثنين', 'الثلاثاء', 'الأربعاء', 'الخميس', 'الجمعة', 'السبت']
    hebrew_day_names = ['ראשון', 'שני', 'שלישי', 'רביעי', 'חמישי', 'שישי', 'שבת']

    for i in range(7):
        current_day = start_of_week + timedelta(days=i)
        week_days.append({
            'date': current_day,
            'arabic_name': day_names[i],
            'hebrew_name': hebrew_day_names[i],
        })

    start_time = datetime.combine(date.today(), time(9, 0))
    end_time = datetime.combine(date.today(), time(22, 0))

    hours = []
    current_time = start_time

    while current_time <= end_time:
        hours.append(current_time.time())
        current_time += timedelta(minutes=75)

    appointments = Appointment.objects.all()
    booked_slots = set((appt.date, appt.time) for appt in appointments)

    schedule = []

    for hour in hours:
        row = {
            'hour': hour.strftime('%H:%M'),
            'slots': []
        }

        for day in week_days:
            is_booked = (day['date'], hour) in booked_slots

            row['slots'].append({
                'date': day['date'],
                'time': hour.strftime('%H:%M'),
                'is_booked': is_booked,
            })

        schedule.append(row)

    return render(request, 'appointments/weekly_schedule.html', {
        'week_days': week_days,
        'schedule': schedule,
        'selected_date': selected_date.strftime('%Y-%m-%d'),
    })

