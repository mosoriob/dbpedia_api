import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MULTIVOLUMEPUBLICATION_TYPE_NAME, MULTIVOLUMEPUBLICATION_TYPE_URI

from openapi_server.models.multi_volume_publication import MultiVolumePublication  # noqa: E501
from openapi_server import util

def multivolumepublications_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of MultiVolumePublication

    Gets a list of all instances of MultiVolumePublication (more information in http://dbpedia.org/ontology/MultiVolumePublication) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[MultiVolumePublication]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MULTIVOLUMEPUBLICATION_TYPE_URI,
        rdf_type_name=MULTIVOLUMEPUBLICATION_TYPE_NAME, 
        kls=MultiVolumePublication)

def multivolumepublications_id_get(id):  # noqa: E501
    """Get a single MultiVolumePublication by its id

    Gets the details of a given MultiVolumePublication (more information in http://dbpedia.org/ontology/MultiVolumePublication) # noqa: E501

    :param id: The ID of the MultiVolumePublication to be retrieved
    :type id: str

    :rtype: MultiVolumePublication
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MULTIVOLUMEPUBLICATION_TYPE_URI,
        rdf_type_name=MULTIVOLUMEPUBLICATION_TYPE_NAME, 
        kls=MultiVolumePublication)
