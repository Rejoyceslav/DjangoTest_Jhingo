from django.shortcuts import render


def word_counter(request):
    return render(request, 'word_counter.html')


def counter_result(request):
    text_to_count = request.POST['text']
    amount_of_words = len(text_to_count.split())
    return render(request, 'counter_result.html', {'amount_of_words': amount_of_words})


def counter_result_deeper(request):
    return render(request, 'counter_result_deeper.html')
