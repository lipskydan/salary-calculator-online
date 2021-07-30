from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import CalcMoneyForm


def main(request):
    salary = five_per_cent_tax = esv = res = 0

    if request.method == 'POST':
        form = CalcMoneyForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            salary = cd['input_money']

            five_per_cent_tax = (salary * 5) / 100
            esv = 1320
            res = salary-five_per_cent_tax-esv

            print(f'salary = {salary}\n five per cent tax = {five_per_cent_tax}\n esv = {esv}')
            print(f'Money to cash = {res}')

            return render(request, 'main/main.html', {'form': form,
                                                      'salary': salary,
                                                      'esv': esv,
                                                      'five_per_cent_tax': five_per_cent_tax,
                                                      'res': res})

    else:
        form = CalcMoneyForm()

    return render(request, 'main/main.html', {'form': form,
                                              'salary': salary,
                                              'esv': esv,
                                              'five_per_cent_tax': five_per_cent_tax,
                                              'res': res})
