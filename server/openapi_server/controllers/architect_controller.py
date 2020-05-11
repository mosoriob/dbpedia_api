import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ARCHITECT_TYPE_NAME, ARCHITECT_TYPE_URI

from openapi_server.models.architect import Architect  # noqa: E501
from openapi_server import util

def architects_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Architect

    Gets a list of all instances of Architect (more information in http://dbpedia.org/ontology/Architect) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Architect]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ARCHITECT_TYPE_URI,
        rdf_type_name=ARCHITECT_TYPE_NAME, 
        kls=Architect)

def architects_id_get(id):  # noqa: E501
    """Get a single Architect by its id

    Gets the details of a given Architect (more information in http://dbpedia.org/ontology/Architect) # noqa: E501

    :param id: The ID of the Architect to be retrieved
    :type id: str

    :rtype: Architect
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ARCHITECT_TYPE_URI,
        rdf_type_name=ARCHITECT_TYPE_NAME, 
        kls=Architect)
