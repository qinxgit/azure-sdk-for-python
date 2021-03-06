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

from .proxy_resource import ProxyResource


class RegisteredServer(ProxyResource):
    """Registered Server resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param server_certificate: Registered Server Certificate
    :type server_certificate: str
    :param agent_version: Registered Server Agent Version
    :type agent_version: str
    :param server_os_version: Registered Server OS Version
    :type server_os_version: str
    :param server_management_error_code: Registered Server Management Error
     Code
    :type server_management_error_code: int
    :param last_heart_beat: Registered Server last heart beat
    :type last_heart_beat: str
    :param provisioning_state: Registered Server Provisioning State
    :type provisioning_state: str
    :param server_role: Registered Server serverRole
    :type server_role: str
    :param cluster_id: Registered Server clusterId
    :type cluster_id: str
    :param cluster_name: Registered Server clusterName
    :type cluster_name: str
    :param server_id: Registered Server serverId
    :type server_id: str
    :param storage_sync_service_uid: Registered Server storageSyncServiceUid
    :type storage_sync_service_uid: str
    :param last_workflow_id: Registered Server lastWorkflowId
    :type last_workflow_id: str
    :param last_operation_name: Resource Last Operation Name
    :type last_operation_name: str
    :param discovery_endpoint_uri: Resource discoveryEndpointUri
    :type discovery_endpoint_uri: str
    :param resource_location: Resource Location
    :type resource_location: str
    :param service_location: Service Location
    :type service_location: str
    :param friendly_name: Friendly Name
    :type friendly_name: str
    :param management_endpoint_uri: Management Endpoint Uri
    :type management_endpoint_uri: str
    :param monitoring_configuration: Monitoring Configuration
    :type monitoring_configuration: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'server_certificate': {'key': 'properties.serverCertificate', 'type': 'str'},
        'agent_version': {'key': 'properties.agentVersion', 'type': 'str'},
        'server_os_version': {'key': 'properties.serverOSVersion', 'type': 'str'},
        'server_management_error_code': {'key': 'properties.serverManagementErrorCode', 'type': 'int'},
        'last_heart_beat': {'key': 'properties.lastHeartBeat', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'server_role': {'key': 'properties.serverRole', 'type': 'str'},
        'cluster_id': {'key': 'properties.clusterId', 'type': 'str'},
        'cluster_name': {'key': 'properties.clusterName', 'type': 'str'},
        'server_id': {'key': 'properties.serverId', 'type': 'str'},
        'storage_sync_service_uid': {'key': 'properties.storageSyncServiceUid', 'type': 'str'},
        'last_workflow_id': {'key': 'properties.lastWorkflowId', 'type': 'str'},
        'last_operation_name': {'key': 'properties.lastOperationName', 'type': 'str'},
        'discovery_endpoint_uri': {'key': 'properties.discoveryEndpointUri', 'type': 'str'},
        'resource_location': {'key': 'properties.resourceLocation', 'type': 'str'},
        'service_location': {'key': 'properties.serviceLocation', 'type': 'str'},
        'friendly_name': {'key': 'properties.friendlyName', 'type': 'str'},
        'management_endpoint_uri': {'key': 'properties.managementEndpointUri', 'type': 'str'},
        'monitoring_configuration': {'key': 'properties.monitoringConfiguration', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RegisteredServer, self).__init__(**kwargs)
        self.server_certificate = kwargs.get('server_certificate', None)
        self.agent_version = kwargs.get('agent_version', None)
        self.server_os_version = kwargs.get('server_os_version', None)
        self.server_management_error_code = kwargs.get('server_management_error_code', None)
        self.last_heart_beat = kwargs.get('last_heart_beat', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.server_role = kwargs.get('server_role', None)
        self.cluster_id = kwargs.get('cluster_id', None)
        self.cluster_name = kwargs.get('cluster_name', None)
        self.server_id = kwargs.get('server_id', None)
        self.storage_sync_service_uid = kwargs.get('storage_sync_service_uid', None)
        self.last_workflow_id = kwargs.get('last_workflow_id', None)
        self.last_operation_name = kwargs.get('last_operation_name', None)
        self.discovery_endpoint_uri = kwargs.get('discovery_endpoint_uri', None)
        self.resource_location = kwargs.get('resource_location', None)
        self.service_location = kwargs.get('service_location', None)
        self.friendly_name = kwargs.get('friendly_name', None)
        self.management_endpoint_uri = kwargs.get('management_endpoint_uri', None)
        self.monitoring_configuration = kwargs.get('monitoring_configuration', None)
