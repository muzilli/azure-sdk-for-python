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


class DiffDiskSettings(Model):
    """Describes the parameters of ephemeral disk settings that can be specified
    for operating system disk. <br><br> NOTE: The ephemeral disk settings can
    only be specified for managed disk.

    :param option: Specifies the ephemeral disk settings for operating system
     disk. Possible values include: 'Local'
    :type option: str or
     ~azure.mgmt.compute.v2018_06_01.models.DiffDiskOptions
    """

    _attribute_map = {
        'option': {'key': 'option', 'type': 'str'},
    }

    def __init__(self, *, option=None, **kwargs) -> None:
        super(DiffDiskSettings, self).__init__(**kwargs)
        self.option = option
