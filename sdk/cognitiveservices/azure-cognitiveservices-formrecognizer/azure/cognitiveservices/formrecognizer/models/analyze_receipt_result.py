# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AnalyzeReceiptResult(Model):
    """Result of the 'Analyze Receipt' operation.

    :param status: Status of the analysis operation. Possible values include:
     'NotStarted', 'Running', 'Failed', 'Succeeded'
    :type status: str or
     ~azure.cognitiveservices.formrecognizer.models.OperationStatusCodes
    :param recognition_results: An array of objects, each representing the OCR
     result for a page in the input document.
    :type recognition_results:
     list[~azure.cognitiveservices.formrecognizer.models.TextRecognitionResult]
    :param understanding_results: An array of objects, each representing a
     receipt detected in the input document.
    :type understanding_results:
     list[~azure.cognitiveservices.formrecognizer.models.UnderstandingResult]
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'OperationStatusCodes'},
        'recognition_results': {'key': 'recognitionResults', 'type': '[TextRecognitionResult]'},
        'understanding_results': {'key': 'understandingResults', 'type': '[UnderstandingResult]'},
    }

    def __init__(self, **kwargs):
        super(AnalyzeReceiptResult, self).__init__(**kwargs)
        self.status = kwargs.get('status', None)
        self.recognition_results = kwargs.get('recognition_results', None)
        self.understanding_results = kwargs.get('understanding_results', None)