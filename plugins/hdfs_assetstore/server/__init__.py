#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
#  Copyright Kitware Inc.
#
#  Licensed under the Apache License, Version 2.0 ( the "License" );
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
###############################################################################

from girder import events
from girder.constants import AssetstoreType
from .assetstore import HdfsAssetstoreAdapter
from .rest import HdfsAssetstoreResource


def getAssetstore(event):
    assetstore = event.info
    if assetstore['type'] == AssetstoreType.HDFS:
        event.stopPropagation()
        event.addResponse(HdfsAssetstoreAdapter(assetstore))


def load(info):
    AssetstoreType.HDFS = 'hdfs'
    events.bind('assetstore.adapter.get', 'hdfs_assetstore', getAssetstore)

    info['apiRoot'].hdfs_assetstore = HdfsAssetstoreResource()
