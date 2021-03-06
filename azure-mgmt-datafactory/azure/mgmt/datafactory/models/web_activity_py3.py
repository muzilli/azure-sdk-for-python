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

from .execution_activity_py3 import ExecutionActivity


class WebActivity(ExecutionActivity):
    """Web activity.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param name: Required. Activity name.
    :type name: str
    :param description: Activity description.
    :type description: str
    :param depends_on: Activity depends on condition.
    :type depends_on: list[~azure.mgmt.datafactory.models.ActivityDependency]
    :param user_properties: Activity user properties.
    :type user_properties: list[~azure.mgmt.datafactory.models.UserProperty]
    :param type: Required. Constant filled by server.
    :type type: str
    :param linked_service_name: Linked service reference.
    :type linked_service_name:
     ~azure.mgmt.datafactory.models.LinkedServiceReference
    :param policy: Activity policy.
    :type policy: ~azure.mgmt.datafactory.models.ActivityPolicy
    :param method: Required. Rest API method for target endpoint. Possible
     values include: 'GET', 'POST', 'PUT', 'DELETE'
    :type method: str or ~azure.mgmt.datafactory.models.WebActivityMethod
    :param url: Required. Web activity target endpoint and path. Type: string
     (or Expression with resultType string).
    :type url: object
    :param headers: Represents the headers that will be sent to the request.
     For example, to set the language and type on a request: "headers" : {
     "Accept-Language": "en-us", "Content-Type": "application/json" }. Type:
     string (or Expression with resultType string).
    :type headers: object
    :param body: Represents the payload that will be sent to the endpoint.
     Required for POST/PUT method, not allowed for GET method Type: string (or
     Expression with resultType string).
    :type body: object
    :param authentication: Authentication method used for calling the
     endpoint.
    :type authentication:
     ~azure.mgmt.datafactory.models.WebActivityAuthentication
    :param datasets: List of datasets passed to web endpoint.
    :type datasets: list[~azure.mgmt.datafactory.models.DatasetReference]
    :param linked_services: List of linked services passed to web endpoint.
    :type linked_services:
     list[~azure.mgmt.datafactory.models.LinkedServiceReference]
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
        'method': {'required': True},
        'url': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'depends_on': {'key': 'dependsOn', 'type': '[ActivityDependency]'},
        'user_properties': {'key': 'userProperties', 'type': '[UserProperty]'},
        'type': {'key': 'type', 'type': 'str'},
        'linked_service_name': {'key': 'linkedServiceName', 'type': 'LinkedServiceReference'},
        'policy': {'key': 'policy', 'type': 'ActivityPolicy'},
        'method': {'key': 'typeProperties.method', 'type': 'str'},
        'url': {'key': 'typeProperties.url', 'type': 'object'},
        'headers': {'key': 'typeProperties.headers', 'type': 'object'},
        'body': {'key': 'typeProperties.body', 'type': 'object'},
        'authentication': {'key': 'typeProperties.authentication', 'type': 'WebActivityAuthentication'},
        'datasets': {'key': 'typeProperties.datasets', 'type': '[DatasetReference]'},
        'linked_services': {'key': 'typeProperties.linkedServices', 'type': '[LinkedServiceReference]'},
    }

    def __init__(self, *, name: str, method, url, additional_properties=None, description: str=None, depends_on=None, user_properties=None, linked_service_name=None, policy=None, headers=None, body=None, authentication=None, datasets=None, linked_services=None, **kwargs) -> None:
        super(WebActivity, self).__init__(additional_properties=additional_properties, name=name, description=description, depends_on=depends_on, user_properties=user_properties, linked_service_name=linked_service_name, policy=policy, **kwargs)
        self.method = method
        self.url = url
        self.headers = headers
        self.body = body
        self.authentication = authentication
        self.datasets = datasets
        self.linked_services = linked_services
        self.type = 'WebActivity'
