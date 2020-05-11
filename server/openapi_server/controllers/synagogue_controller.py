import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SYNAGOGUE_TYPE_NAME, SYNAGOGUE_TYPE_URI

from openapi_server.models.synagogue import Synagogue  # noqa: E501
from openapi_server import util

def synagogues_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Synagogue

    Gets a list of all instances of Synagogue (more information in http://dbpedia.org/ontology/Synagogue) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Synagogue]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SYNAGOGUE_TYPE_URI,
        rdf_type_name=SYNAGOGUE_TYPE_NAME, 
        kls=Synagogue)

def synagogues_id_get(id):  # noqa: E501
    """Get a single Synagogue by its id

    Gets the details of a given Synagogue (more information in http://dbpedia.org/ontology/Synagogue) # noqa: E501

    :param id: The ID of the Synagogue to be retrieved
    :type id: str

    :rtype: Synagogue
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SYNAGOGUE_TYPE_URI,
        rdf_type_name=SYNAGOGUE_TYPE_NAME, 
        kls=Synagogue)
