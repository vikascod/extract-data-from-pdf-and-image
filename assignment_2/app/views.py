from django.shortcuts import render
from pdfminer.high_level import extract_text
from io import BytesIO
from functools import lru_cache


@lru_cache(maxsize=None)
def home(request):
    if request.method == "POST":
        pdf_file = request.FILES['pdf_file']
        pdf_content = BytesIO(pdf_file.read())
        extracted_data = extract_text(pdf_content)

        context = {
            'extracted_data':extracted_data
        }
        return render(request, 'app/home.html', context)
    return render(request, 'app/home.html')
