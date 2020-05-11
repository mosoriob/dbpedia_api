import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MOUNTAINRANGE_TYPE_NAME, MOUNTAINRANGE_TYPE_URI

from openapi_server.models.mountain_range import MountainRange  # noqa: E501
from openapi_server import util

def mountainranges_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of MountainRange

    Gets a list of all instances of MountainRange (more information in http://dbpedia.org/ontology/MountainRange) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[MountainRange]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MOUNTAINRANGE_TYPE_URI,
        rdf_type_name=MOUNTAINRANGE_TYPE_NAME, 
        kls=MountainRange)

def mountainranges_id_get(id):  # noqa: E501
    """Get a single MountainRange by its id

    Gets the details of a given MountainRange (more information in http://dbpedia.org/ontology/MountainRange) # noqa: E501

    :param id: The ID of the MountainRange to be retrieved
    :type id: str

    :rtype: MountainRange
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MOUNTAINRANGE_TYPE_URI,
        rdf_type_name=MOUNTAINRANGE_TYPE_NAME, 
        kls=MountainRange)
