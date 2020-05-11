import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PRESIDENT_TYPE_NAME, PRESIDENT_TYPE_URI

from openapi_server.models.president import President  # noqa: E501
from openapi_server import util

def presidents_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of President

    Gets a list of all instances of President (more information in http://dbpedia.org/ontology/President) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[President]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PRESIDENT_TYPE_URI,
        rdf_type_name=PRESIDENT_TYPE_NAME, 
        kls=President)

def presidents_id_get(id):  # noqa: E501
    """Get a single President by its id

    Gets the details of a given President (more information in http://dbpedia.org/ontology/President) # noqa: E501

    :param id: The ID of the President to be retrieved
    :type id: str

    :rtype: President
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PRESIDENT_TYPE_URI,
        rdf_type_name=PRESIDENT_TYPE_NAME, 
        kls=President)
