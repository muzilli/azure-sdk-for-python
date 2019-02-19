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


class SizeAvailability(Model):
    """Represents the size information.

    :param size_category: The category of the size (Basic, Standard,
     Performance). Possible values include: 'Basic', 'Standard', 'Performance'
    :type size_category: str or
     ~azure.mgmt.labservices.models.ManagedLabVmSize
    :param is_available: Whether or not this size category is available
    :type is_available: bool
    """

    _attribute_map = {
        'size_category': {'key': 'sizeCategory', 'type': 'str'},
        'is_available': {'key': 'isAvailable', 'type': 'bool'},
    }

    def __init__(self, *, size_category=None, is_available: bool=None, **kwargs) -> None:
        super(SizeAvailability, self).__init__(**kwargs)
        self.size_category = size_category
        self.is_available = is_available
