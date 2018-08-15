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

from .resource_py3 import Resource


class SubscriptionContract(Resource):
    """Subscription details.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type for API Management resource.
    :vartype type: str
    :param user_id: Required. The user resource identifier of the subscription
     owner. The value is a valid relative URL in the format of /users/{uid}
     where {uid} is a user identifier.
    :type user_id: str
    :param product_id: Required. The product resource identifier of the
     subscribed product. The value is a valid relative URL in the format of
     /products/{productId} where {productId} is a product identifier.
    :type product_id: str
    :param display_name: The name of the subscription, or null if the
     subscription has no name.
    :type display_name: str
    :param state: Required. Subscription state. Possible states are * active –
     the subscription is active, * suspended – the subscription is blocked, and
     the subscriber cannot call any APIs of the product, * submitted – the
     subscription request has been made by the developer, but has not yet been
     approved or rejected, * rejected – the subscription request has been
     denied by an administrator, * cancelled – the subscription has been
     cancelled by the developer or administrator, * expired – the subscription
     reached its expiration date and was deactivated. Possible values include:
     'suspended', 'active', 'expired', 'submitted', 'rejected', 'cancelled'
    :type state: str or ~azure.mgmt.apimanagement.models.SubscriptionState
    :ivar created_date: Subscription creation date. The date conforms to the
     following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601
     standard.
    :vartype created_date: datetime
    :param start_date: Subscription activation date. The setting is for audit
     purposes only and the subscription is not automatically activated. The
     subscription lifecycle can be managed by using the `state` property. The
     date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified
     by the ISO 8601 standard.
    :type start_date: datetime
    :param expiration_date: Subscription expiration date. The setting is for
     audit purposes only and the subscription is not automatically expired. The
     subscription lifecycle can be managed by using the `state` property. The
     date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified
     by the ISO 8601 standard.
    :type expiration_date: datetime
    :param end_date: Date when subscription was cancelled or expired. The
     setting is for audit purposes only and the subscription is not
     automatically cancelled. The subscription lifecycle can be managed by
     using the `state` property. The date conforms to the following format:
     `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.
    :type end_date: datetime
    :param notification_date: Upcoming subscription expiration notification
     date. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as
     specified by the ISO 8601 standard.
    :type notification_date: datetime
    :param primary_key: Required. Subscription primary key.
    :type primary_key: str
    :param secondary_key: Required. Subscription secondary key.
    :type secondary_key: str
    :param state_comment: Optional subscription comment added by an
     administrator.
    :type state_comment: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'user_id': {'required': True},
        'product_id': {'required': True},
        'display_name': {'max_length': 100, 'min_length': 0},
        'state': {'required': True},
        'created_date': {'readonly': True},
        'primary_key': {'required': True, 'max_length': 256, 'min_length': 1},
        'secondary_key': {'required': True, 'max_length': 256, 'min_length': 1},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'user_id': {'key': 'properties.userId', 'type': 'str'},
        'product_id': {'key': 'properties.productId', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'state': {'key': 'properties.state', 'type': 'SubscriptionState'},
        'created_date': {'key': 'properties.createdDate', 'type': 'iso-8601'},
        'start_date': {'key': 'properties.startDate', 'type': 'iso-8601'},
        'expiration_date': {'key': 'properties.expirationDate', 'type': 'iso-8601'},
        'end_date': {'key': 'properties.endDate', 'type': 'iso-8601'},
        'notification_date': {'key': 'properties.notificationDate', 'type': 'iso-8601'},
        'primary_key': {'key': 'properties.primaryKey', 'type': 'str'},
        'secondary_key': {'key': 'properties.secondaryKey', 'type': 'str'},
        'state_comment': {'key': 'properties.stateComment', 'type': 'str'},
    }

    def __init__(self, *, user_id: str, product_id: str, state, primary_key: str, secondary_key: str, display_name: str=None, start_date=None, expiration_date=None, end_date=None, notification_date=None, state_comment: str=None, **kwargs) -> None:
        super(SubscriptionContract, self).__init__(**kwargs)
        self.user_id = user_id
        self.product_id = product_id
        self.display_name = display_name
        self.state = state
        self.created_date = None
        self.start_date = start_date
        self.expiration_date = expiration_date
        self.end_date = end_date
        self.notification_date = notification_date
        self.primary_key = primary_key
        self.secondary_key = secondary_key
        self.state_comment = state_comment