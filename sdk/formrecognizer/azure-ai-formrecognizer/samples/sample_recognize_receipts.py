# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_recognize_receipts.py

DESCRIPTION:
    This sample demonstrates how to recognize US sales receipts from a file.

USAGE:
    python sample_recognize_receipts.py

    Set the environment variables with your own values before running the sample:
    1) AZURE_FORM_RECOGNIZER_ENDPOINT - the endpoint to your Cognitive Services resource.
    2) AZURE_FORM_RECOGNIZER_KEY - your Form Recognizer API key
"""

import os


class RecognizeReceiptsSample(object):

    def recognize_receipts(self):
        path_to_sample_forms = os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "./sample_forms/receipt/contoso-allinone.jpg"))
        # [START recognize_receipts]
        from azure.core.credentials import AzureKeyCredential
        from azure.ai.formrecognizer import FormRecognizerClient

        endpoint = os.environ["AZURE_FORM_RECOGNIZER_ENDPOINT"]
        key = os.environ["AZURE_FORM_RECOGNIZER_KEY"]

        form_recognizer_client = FormRecognizerClient(
            endpoint=endpoint, credential=AzureKeyCredential(key)
        )
        with open(path_to_sample_forms, "rb") as f:
            poller = form_recognizer_client.begin_recognize_receipts(receipt=f)
        receipts = poller.result()

        for idx, receipt in enumerate(receipts):
            print("--------Recognizing receipt #{}--------".format(idx))
            receipt_type = receipt.fields.get("ReceiptType")
            if receipt_type:
                print("Receipt Type: {} has confidence: {}".format(receipt_type.value, receipt_type.confidence))
            merchant_name = receipt.fields.get("MerchantName")
            if merchant_name:
                print("Merchant Name: {} has confidence: {}".format(merchant_name.value, merchant_name.confidence))
            transaction_date = receipt.fields.get("TransactionDate")
            if transaction_date:
                print("Transaction Date: {} has confidence: {}".format(transaction_date.value, transaction_date.confidence))
            print("Receipt items:")
            for idx, item in enumerate(receipt.fields.get("Items").value):
                print("...Item #{}".format(idx))
                item_name = item.value.get("Name")
                if item_name:
                    print("......Item Name: {} has confidence: {}".format(item_name.value, item_name.confidence))
                item_quantity = item.value.get("Quantity")
                if item_quantity:
                    print("......Item Quantity: {} has confidence: {}".format(item_quantity.value, item_quantity.confidence))
                item_price = item.value.get("Price")
                if item_price:
                    print("......Individual Item Price: {} has confidence: {}".format(item_price.value, item_price.confidence))
                item_total_price = item.value.get("TotalPrice")
                if item_total_price:
                    print("......Total Item Price: {} has confidence: {}".format(item_total_price.value, item_total_price.confidence))
            subtotal = receipt.fields.get("Subtotal")
            if subtotal:
                print("Subtotal: {} has confidence: {}".format(subtotal.value, subtotal.confidence))
            tax = receipt.fields.get("Tax")
            if tax:
                print("Tax: {} has confidence: {}".format(tax.value, tax.confidence))
            tip = receipt.fields.get("Tip")
            if tip:
                print("Tip: {} has confidence: {}".format(tip.value, tip.confidence))
            total = receipt.fields.get("Total")
            if total:
                print("Total: {} has confidence: {}".format(total.value, total.confidence))
            print("--------------------------------------")
        # [END recognize_receipts]


if __name__ == '__main__':
    sample = RecognizeReceiptsSample()
    sample.recognize_receipts()
