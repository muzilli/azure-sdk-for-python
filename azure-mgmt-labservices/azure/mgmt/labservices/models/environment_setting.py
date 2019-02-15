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

from .resource import Resource


class EnvironmentSetting(Resource):
    """Represents settings of an environment, from which environment instances
    would be created.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The identifier of the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param location: The location of the resource.
    :type location: str
    :param tags: The tags of the resource.
    :type tags: dict[str, str]
    :ivar publishing_state: Describes the readiness of this environment
     setting. Possible values include: 'Draft', 'Publishing', 'Published',
     'PublishFailed', 'Scaling'
    :vartype publishing_state: str or
     ~azure.mgmt.labservices.models.PublishingState
    :param configuration_state: Describes the user's progress in configuring
     their environment setting. Possible values include: 'NotApplicable',
     'Completed'
    :type configuration_state: str or
     ~azure.mgmt.labservices.models.ConfigurationState
    :param description: Describes the environment and its resource settings
    :type description: str
    :param title: Brief title describing the environment and its resource
     settings
    :type title: str
    :param resource_settings: Required. The resource specific settings
    :type resource_settings: ~azure.mgmt.labservices.models.ResourceSettings
    :ivar last_changed: Time when the template VM was last changed.
    :vartype last_changed: datetime
    :ivar last_published: Time when the template VM was last sent for
     publishing.
    :vartype last_published: datetime
    :param provisioning_state: The provisioning status of the resource.
    :type provisioning_state: str
    :param unique_identifier: The unique immutable identifier of a resource
     (Guid).
    :type unique_identifier: str
    :ivar latest_operation_result: The details of the latest operation. ex:
     status, error
    :vartype latest_operation_result:
     ~azure.mgmt.labservices.models.LatestOperationResult
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'publishing_state': {'readonly': True},
        'resource_settings': {'required': True},
        'last_changed': {'readonly': True},
        'last_published': {'readonly': True},
        'latest_operation_result': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'publishing_state': {'key': 'properties.publishingState', 'type': 'str'},
        'configuration_state': {'key': 'properties.configurationState', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'title': {'key': 'properties.title', 'type': 'str'},
        'resource_settings': {'key': 'properties.resourceSettings', 'type': 'ResourceSettings'},
        'last_changed': {'key': 'properties.lastChanged', 'type': 'iso-8601'},
        'last_published': {'key': 'properties.lastPublished', 'type': 'iso-8601'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'unique_identifier': {'key': 'properties.uniqueIdentifier', 'type': 'str'},
        'latest_operation_result': {'key': 'properties.latestOperationResult', 'type': 'LatestOperationResult'},
    }

    def __init__(self, **kwargs):
        super(EnvironmentSetting, self).__init__(**kwargs)
        self.publishing_state = None
        self.configuration_state = kwargs.get('configuration_state', None)
        self.description = kwargs.get('description', None)
        self.title = kwargs.get('title', None)
        self.resource_settings = kwargs.get('resource_settings', None)
        self.last_changed = None
        self.last_published = None
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.unique_identifier = kwargs.get('unique_identifier', None)
        self.latest_operation_result = None
