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


class Line(Model):
    """An object representing a recognized text line.

    :param bounding_box: Bounding box of a recognized line.
    :type bounding_box: list[int]
    :param text: The text content of the line.
    :type text: str
    :param words: List of words in the text line.
    :type words:
     list[~azure.cognitiveservices.vision.computervision.models.Word]
    """

    _attribute_map = {
        'bounding_box': {'key': 'boundingBox', 'type': '[int]'},
        'text': {'key': 'text', 'type': 'str'},
        'words': {'key': 'words', 'type': '[Word]'},
    }

    def __init__(self, **kwargs):
        super(Line, self).__init__(**kwargs)
        self.bounding_box = kwargs.get('bounding_box', None)
        self.text = kwargs.get('text', None)
        self.words = kwargs.get('words', None)
