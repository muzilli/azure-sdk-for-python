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

from .artifact_py3 import Artifact


class TemplateArtifact(Artifact):
    """Blueprint artifact deploys Azure resource manager template.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: String Id used to locate any resource on Azure.
    :vartype id: str
    :ivar type: Type of this resource.
    :vartype type: str
    :ivar name: Name of this resource.
    :vartype name: str
    :param kind: Required. Constant filled by server.
    :type kind: str
    :param display_name: One-liner string explain this resource.
    :type display_name: str
    :param description: Multi-line explain this resource.
    :type description: str
    :param depends_on: Artifacts which need to be deployed before the
     specified artifact.
    :type depends_on: list[str]
    :param template: Required. The Azure Resource Manager template body.
    :type template: object
    :param resource_group: If applicable, the name of the resource group
     placeholder to which the template will be deployed.
    :type resource_group: str
    :param parameters: Required. Template parameter values.
    :type parameters: dict[str,
     ~azure.mgmt.blueprint.models.ParameterValueBase]
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
        'kind': {'required': True},
        'display_name': {'max_length': 256},
        'description': {'max_length': 500},
        'template': {'required': True},
        'parameters': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'depends_on': {'key': 'properties.dependsOn', 'type': '[str]'},
        'template': {'key': 'properties.template', 'type': 'object'},
        'resource_group': {'key': 'properties.resourceGroup', 'type': 'str'},
        'parameters': {'key': 'properties.parameters', 'type': '{ParameterValueBase}'},
    }

    def __init__(self, *, template, parameters, display_name: str=None, description: str=None, depends_on=None, resource_group: str=None, **kwargs) -> None:
        super(TemplateArtifact, self).__init__(**kwargs)
        self.display_name = display_name
        self.description = description
        self.depends_on = depends_on
        self.template = template
        self.resource_group = resource_group
        self.parameters = parameters
        self.kind = 'template'