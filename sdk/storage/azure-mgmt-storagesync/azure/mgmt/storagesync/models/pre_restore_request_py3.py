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


class PreRestoreRequest(Model):
    """Pre Restore request object.

    :param partition: Pre Restore partition.
    :type partition: str
    :param replica_group: Pre Restore replica group.
    :type replica_group: str
    :param request_id: Pre Restore request id.
    :type request_id: str
    :param azure_file_share_uri: Pre Restore Azure file share uri.
    :type azure_file_share_uri: str
    :param status: Pre Restore Azure status.
    :type status: str
    :param source_azure_file_share_uri: Pre Restore Azure source azure file
     share uri.
    :type source_azure_file_share_uri: str
    :param backup_metadata_property_bag: Pre Restore backup metadata property
     bag.
    :type backup_metadata_property_bag: str
    :param restore_file_spec: Pre Restore restore file spec array.
    :type restore_file_spec:
     list[~azure.mgmt.storagesync.models.RestoreFileSpec]
    :param pause_wait_for_sync_drain_time_period_in_seconds: Pre Restore pause
     wait for sync drain time period in seconds.
    :type pause_wait_for_sync_drain_time_period_in_seconds: int
    """

    _attribute_map = {
        'partition': {'key': 'partition', 'type': 'str'},
        'replica_group': {'key': 'replicaGroup', 'type': 'str'},
        'request_id': {'key': 'requestId', 'type': 'str'},
        'azure_file_share_uri': {'key': 'azureFileShareUri', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'source_azure_file_share_uri': {'key': 'sourceAzureFileShareUri', 'type': 'str'},
        'backup_metadata_property_bag': {'key': 'backupMetadataPropertyBag', 'type': 'str'},
        'restore_file_spec': {'key': 'restoreFileSpec', 'type': '[RestoreFileSpec]'},
        'pause_wait_for_sync_drain_time_period_in_seconds': {'key': 'pauseWaitForSyncDrainTimePeriodInSeconds', 'type': 'int'},
    }

    def __init__(self, *, partition: str=None, replica_group: str=None, request_id: str=None, azure_file_share_uri: str=None, status: str=None, source_azure_file_share_uri: str=None, backup_metadata_property_bag: str=None, restore_file_spec=None, pause_wait_for_sync_drain_time_period_in_seconds: int=None, **kwargs) -> None:
        super(PreRestoreRequest, self).__init__(**kwargs)
        self.partition = partition
        self.replica_group = replica_group
        self.request_id = request_id
        self.azure_file_share_uri = azure_file_share_uri
        self.status = status
        self.source_azure_file_share_uri = source_azure_file_share_uri
        self.backup_metadata_property_bag = backup_metadata_property_bag
        self.restore_file_spec = restore_file_spec
        self.pause_wait_for_sync_drain_time_period_in_seconds = pause_wait_for_sync_drain_time_period_in_seconds
