import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CHURCH_TYPE_NAME, CHURCH_TYPE_URI

from openapi_server.models.church import Church  # noqa: E501
from openapi_server import util

def churchs_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Church

    Gets a list of all instances of Church (more information in http://dbpedia.org/ontology/Church) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Church]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CHURCH_TYPE_URI,
        rdf_type_name=CHURCH_TYPE_NAME, 
        kls=Church)

def churchs_id_get(id):  # noqa: E501
    """Get a single Church by its id

    Gets the details of a given Church (more information in http://dbpedia.org/ontology/Church) # noqa: E501

    :param id: The ID of the Church to be retrieved
    :type id: str

    :rtype: Church
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CHURCH_TYPE_URI,
        rdf_type_name=CHURCH_TYPE_NAME, 
        kls=Church)
