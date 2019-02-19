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


class IPRule(Model):
    """IP rule with specific IP or IP range in CIDR format.

    All required parameters must be populated in order to send to Azure.

    :param action: The action of IP ACL rule. Possible values include:
     'Allow'. Default value: "Allow" .
    :type action: str or
     ~azure.mgmt.containerregistry.v2018_02_01_preview.models.Action
    :param ip_address_or_range: Required. Specifies the IP or IP range in CIDR
     format. Only IPV4 address is allowed.
    :type ip_address_or_range: str
    """

    _validation = {
        'ip_address_or_range': {'required': True},
    }

    _attribute_map = {
        'action': {'key': 'action', 'type': 'str'},
        'ip_address_or_range': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(IPRule, self).__init__(**kwargs)
        self.action = kwargs.get('action', "Allow")
        self.ip_address_or_range = kwargs.get('ip_address_or_range', None)
