import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import COMEDIAN_TYPE_NAME, COMEDIAN_TYPE_URI

from openapi_server.models.comedian import Comedian  # noqa: E501
from openapi_server import util

def comedians_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Comedian

    Gets a list of all instances of Comedian (more information in http://dbpedia.org/ontology/Comedian) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Comedian]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=COMEDIAN_TYPE_URI,
        rdf_type_name=COMEDIAN_TYPE_NAME, 
        kls=Comedian)

def comedians_id_get(id):  # noqa: E501
    """Get a single Comedian by its id

    Gets the details of a given Comedian (more information in http://dbpedia.org/ontology/Comedian) # noqa: E501

    :param id: The ID of the Comedian to be retrieved
    :type id: str

    :rtype: Comedian
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=COMEDIAN_TYPE_URI,
        rdf_type_name=COMEDIAN_TYPE_NAME, 
        kls=Comedian)
