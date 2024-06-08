from django.shortcuts import render
from django.http import JsonResponse
from .forms import MyForm

def average(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['numbers']
            try:
                numbers = list(map(float, data.split(',')))
                if len(numbers) != 10:
                    raise ValueError("Exactly 10 numbers are required.")
                average = sum(numbers) / len(numbers)
                return JsonResponse({'average': average})
            except ValueError as e:
                return JsonResponse({'error': str(e)}, status=400)
    else:
        form = MyForm()

    return render(request, 'myapp/average.html', {'form': form})