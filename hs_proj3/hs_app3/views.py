from django.shortcuts import render
import json
import Bio
from Bio.Seq import Seq
from Bio.SeqUtils import MeltingTemp as mt

# Create your views here.
def input(request):
    """
    Render the input page.
    """
    context = {
        'message': 'Please enter your data below.'
    }
    return render(request, 'input.html', context)

def result(request):
    """
    Process the input data and render the result page.
    """
    if request.method == 'POST':
        # Assuming the form data is sent as POST
        input_data = request.POST["hot_data"]
        rec_data = json.loads(input_data)
        print("Received data:", rec_data)
        print("length of rec_data:", len(rec_data))
        for row in rec_data:
            print("Row data:", row)
            row.append(str(Seq(row[1]).reverse_complement()))
            row.append('%0.2f' % mt.Tm_NN(Seq(row[1]), nn_table=mt.DNA_NN1))

        context = {

            'rec_data': rec_data,
            'message': 'Here is the result of your input.'
        }
    else:
        context = {
            'message': 'No data submitted.'
        }
    
    return render(request, 'result.html', context)