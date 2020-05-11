import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GIVENNAME_TYPE_NAME, GIVENNAME_TYPE_URI

from openapi_server.models.given_name import GivenName  # noqa: E501
from openapi_server import util

def givennames_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of GivenName

    Gets a list of all instances of GivenName (more information in http://dbpedia.org/ontology/GivenName) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[GivenName]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GIVENNAME_TYPE_URI,
        rdf_type_name=GIVENNAME_TYPE_NAME, 
        kls=GivenName)

def givennames_id_get(id):  # noqa: E501
    """Get a single GivenName by its id

    Gets the details of a given GivenName (more information in http://dbpedia.org/ontology/GivenName) # noqa: E501

    :param id: The ID of the GivenName to be retrieved
    :type id: str

    :rtype: GivenName
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GIVENNAME_TYPE_URI,
        rdf_type_name=GIVENNAME_TYPE_NAME, 
        kls=GivenName)
