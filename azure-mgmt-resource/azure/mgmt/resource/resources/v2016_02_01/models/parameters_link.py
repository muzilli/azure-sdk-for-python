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


class ParametersLink(Model):
    """Entity representing the reference to the deployment parameters.

    All required parameters must be populated in order to send to Azure.

    :param uri: Required. URI referencing the template.
    :type uri: str
    :param content_version: If included it must match the ContentVersion in
     the template.
    :type content_version: str
    """

    _validation = {
        'uri': {'required': True},
    }

    _attribute_map = {
        'uri': {'key': 'uri', 'type': 'str'},
        'content_version': {'key': 'contentVersion', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ParametersLink, self).__init__(**kwargs)
        self.uri = kwargs.get('uri', None)
        self.content_version = kwargs.get('content_version', None)
