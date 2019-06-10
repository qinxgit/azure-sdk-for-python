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


class IdentityProperties(Model):
    """Managed identity for the resource.

    :param principal_id: The principal ID of resource identity.
    :type principal_id: str
    :param tenant_id: The tenant ID of resource.
    :type tenant_id: str
    :param type: The identity type. Possible values include: 'SystemAssigned',
     'UserAssigned', 'SystemAssigned, UserAssigned', 'None'
    :type type: str or
     ~azure.mgmt.containerregistry.v2019_04_01.models.ResourceIdentityType
    :param user_assigned_identities: The list of user identities associated
     with the resource. The user identity
     dictionary key references will be ARM resource ids in the form:
     '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/
     providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
    :type user_assigned_identities: dict[str,
     ~azure.mgmt.containerregistry.v2019_04_01.models.UserIdentityProperties]
    """

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'ResourceIdentityType'},
        'user_assigned_identities': {'key': 'userAssignedIdentities', 'type': '{UserIdentityProperties}'},
    }

    def __init__(self, **kwargs):
        super(IdentityProperties, self).__init__(**kwargs)
        self.principal_id = kwargs.get('principal_id', None)
        self.tenant_id = kwargs.get('tenant_id', None)
        self.type = kwargs.get('type', None)
        self.user_assigned_identities = kwargs.get('user_assigned_identities', None)