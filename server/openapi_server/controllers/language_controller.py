import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import LANGUAGE_TYPE_NAME, LANGUAGE_TYPE_URI

from openapi_server.models.language import Language  # noqa: E501
from openapi_server import util

def languages_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Language

    Gets a list of all instances of Language (more information in http://dbpedia.org/ontology/Language) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Language]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=LANGUAGE_TYPE_URI,
        rdf_type_name=LANGUAGE_TYPE_NAME, 
        kls=Language)

def languages_id_get(id):  # noqa: E501
    """Get a single Language by its id

    Gets the details of a given Language (more information in http://dbpedia.org/ontology/Language) # noqa: E501

    :param id: The ID of the Language to be retrieved
    :type id: str

    :rtype: Language
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=LANGUAGE_TYPE_URI,
        rdf_type_name=LANGUAGE_TYPE_NAME, 
        kls=Language)
