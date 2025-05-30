from django.shortcuts import render
from Bio.Seq import Seq

# Create your views here.
def hello(request):
    """
    A simple view that returns a greeting.
    """
    return render(request, 'hello.html', {'greeting': 'Hello, World! Again!!'})

def start(request):
    return render(request, "input.html")

def revcomp(request):
    seq = Seq(request.POST["sequence"])
    revcomp = seq.reverse_complement()

    return render(request, "result.html", {"result": revcomp})