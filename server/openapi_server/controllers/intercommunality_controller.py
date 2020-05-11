import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import INTERCOMMUNALITY_TYPE_NAME, INTERCOMMUNALITY_TYPE_URI

from openapi_server.models.intercommunality import Intercommunality  # noqa: E501
from openapi_server import util

def intercommunalitys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Intercommunality

    Gets a list of all instances of Intercommunality (more information in http://dbpedia.org/ontology/Intercommunality) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Intercommunality]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=INTERCOMMUNALITY_TYPE_URI,
        rdf_type_name=INTERCOMMUNALITY_TYPE_NAME, 
        kls=Intercommunality)

def intercommunalitys_id_get(id):  # noqa: E501
    """Get a single Intercommunality by its id

    Gets the details of a given Intercommunality (more information in http://dbpedia.org/ontology/Intercommunality) # noqa: E501

    :param id: The ID of the Intercommunality to be retrieved
    :type id: str

    :rtype: Intercommunality
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=INTERCOMMUNALITY_TYPE_URI,
        rdf_type_name=INTERCOMMUNALITY_TYPE_NAME, 
        kls=Intercommunality)
