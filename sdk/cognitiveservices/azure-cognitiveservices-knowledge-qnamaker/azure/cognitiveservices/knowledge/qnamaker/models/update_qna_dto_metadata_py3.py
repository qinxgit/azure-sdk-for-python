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

from .update_metadata_dto_py3 import UpdateMetadataDTO


class UpdateQnaDTOMetadata(UpdateMetadataDTO):
    """List of metadata associated with the answer to be updated.

    :param delete: List of Metadata associated with answer to be deleted
    :type delete:
     list[~azure.cognitiveservices.knowledge.qnamaker.models.MetadataDTO]
    :param add: List of metadata associated with answer to be added
    :type add:
     list[~azure.cognitiveservices.knowledge.qnamaker.models.MetadataDTO]
    """

    _attribute_map = {
        'delete': {'key': 'delete', 'type': '[MetadataDTO]'},
        'add': {'key': 'add', 'type': '[MetadataDTO]'},
    }

    def __init__(self, *, delete=None, add=None, **kwargs) -> None:
        super(UpdateQnaDTOMetadata, self).__init__(delete=delete, add=add, **kwargs)
