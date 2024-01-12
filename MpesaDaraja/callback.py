import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # Add this import


@csrf_exempt  # Decorate the view to disable CSRF protection for testing purposes
def process_stk_callback(request):
    if request.method == 'POST':
        try:
            # Load the STK callback response from the request body
            stk_callback_response = json.loads(request.body.decode('utf-8'))
            # Save the response to a log file
            log_file = "Mpesastkresponse.json"
            # with open(log_file, "a") as log:
            json.dump(stk_callback_response, log)

             # Method Not Allowed

    # # Extract data from the response
            merchant_request_id = stk_callback_response['Body']['stkCallback']['MerchantRequestID']
    # checkout_request_id = stk_callback_response['Body']['stkCallback']['CheckoutRequestID']
    # result_code = stk_callback_response['Body']['stkCallback']['ResultCode']
    # result_desc = stk_callback_response['Body']['stkCallback']['ResultDesc']
    # amount = stk_callback_response['Body']['stkCallback']['CallbackMetadata']['Item'][0]['Value']
    # transaction_id = stk_callback_response['Body']['stkCallback']['CallbackMetadata']['Item'][1]['Value']
    # user_phone_number = stk_callback_response['Body']['stkCallback']['CallbackMetadata']['Item'][4]['Value']

    # # Check if the result_code is 0
    # if result_code == 0:
    #     # Perform your actions here for a successful transaction
    #     # For example, you can update your database or trigger some other process.
    #     # You can add your code here to handle a successful transaction.

    #     # You can return a success response to the STK callback, for example:
    #     response_data = {
    #         "ResultCode": "0",
    #         "ResultDesc": "Transaction successful"
    #     }
    #     return JsonResponse(response_data)
    # else:
    #     # Handle other result_code values (not 0) here if needed
    #     # You can return an appropriate response for failed transactions.
    #     response_data = {
    #         "ResultCode": result_code,
    #         "ResultDesc": result_desc
    #     }
    #     return JsonResponse(response_data)
        except json.JSONDecodeError as e: 
    #         return JsonResponse({'error': 'Failed to decode JSON', 'detail': str(e)}, status=400)
    # else:
        # Method/ Not Allowed
         return JsonResponse({'error': 'Failed to decode JSON', 'detail': str(e)}, status=400)
