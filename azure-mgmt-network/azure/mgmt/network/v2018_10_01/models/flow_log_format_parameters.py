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


class FlowLogFormatParameters(Model):
    """Parameters that define the flow log format.

    :param type: The file type of flow log. Possible values include: 'JSON'
    :type type: str or
     ~azure.mgmt.network.v2018_10_01.models.FlowLogFormatType
    :param version: The version (revision) of the flow log. Default value: 0 .
    :type version: int
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'version': {'key': 'version', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(FlowLogFormatParameters, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.version = kwargs.get('version', 0)