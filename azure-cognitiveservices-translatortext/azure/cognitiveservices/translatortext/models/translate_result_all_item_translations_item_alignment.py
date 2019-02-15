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


class TranslateResultAllItemTranslationsItemAlignment(Model):
    """TranslateResultAllItemTranslationsItemAlignment.

    :param proj:
    :type proj: str
    """

    _attribute_map = {
        'proj': {'key': 'proj', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(TranslateResultAllItemTranslationsItemAlignment, self).__init__(**kwargs)
        self.proj = kwargs.get('proj', None)