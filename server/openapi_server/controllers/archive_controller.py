import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ARCHIVE_TYPE_NAME, ARCHIVE_TYPE_URI

from openapi_server.models.archive import Archive  # noqa: E501
from openapi_server import util

def archives_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Archive

    Gets a list of all instances of Archive (more information in http://dbpedia.org/ontology/Archive) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Archive]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ARCHIVE_TYPE_URI,
        rdf_type_name=ARCHIVE_TYPE_NAME, 
        kls=Archive)

def archives_id_get(id):  # noqa: E501
    """Get a single Archive by its id

    Gets the details of a given Archive (more information in http://dbpedia.org/ontology/Archive) # noqa: E501

    :param id: The ID of the Archive to be retrieved
    :type id: str

    :rtype: Archive
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ARCHIVE_TYPE_URI,
        rdf_type_name=ARCHIVE_TYPE_NAME, 
        kls=Archive)
