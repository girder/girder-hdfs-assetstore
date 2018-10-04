HDFS Assetstore
---------------

This plugin creates a new type of assetstore that can be used to store and
proxy data on a Hadoop Distributed Filesystem. An HDFS assetstore can be used
to import existing HDFS data hierarchies into the Girder data hierarchy, and
it can also serve as a normal assetstore that stores and manages files created
via Girder's interface.

.. note:: Deleting files that were imported from existing HDFS files does not
  delete the original file from HDFS, they will simply be unlinked in the
  Girder hierarchy.

Once you enable the plugin, site administrators will be able to create and edit
HDFS assetstores on the ``Assetstores`` page in the web client in the same way
as any other assetstore type. When creating or editing an assetstore, validation
is performed to ensure that the HDFS instance is reachable for communication, and
that the directory specified as the root path exists. If it does not exist, Girder
will attempt to create it.

Importing data
**************

Once you have created an HDFS assetstore, you will be able to import data
into it on demand if you have site administrator privileges. In the assetstore
list in the web client, you will see an **Import** button next to your HDFS
assetstores that will allow you to import files or directories (recursively)
from that HDFS instance into a Girder user, collection, or folder of your choice.

You should specify an absolute data path when importing; the root path that you
chose for your assetstore is not used in the import process. Each directory
imported will become a folder in Girder, and each file will become an item with
a single file inside. Once imported, file data is proxied through Girder when
being downloaded, but still must reside in the same location on HDFS.

Duplicates (that is, pre-existing files with the same name in the same location
in the Girder hierarchy) will be ignored if, for instance, you import the same
hierarchy into the same location twice in a row.
