import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ORGANISATION_TYPE_NAME, ORGANISATION_TYPE_URI

from openapi_server.models.organisation import Organisation  # noqa: E501
from openapi_server import util

def organisations_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Organisation

    Gets a list of all instances of Organisation (more information in http://dbpedia.org/ontology/Organisation) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Organisation]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ORGANISATION_TYPE_URI,
        rdf_type_name=ORGANISATION_TYPE_NAME, 
        kls=Organisation)

def organisations_id_get(id):  # noqa: E501
    """Get a single Organisation by its id

    Gets the details of a given Organisation (more information in http://dbpedia.org/ontology/Organisation) # noqa: E501

    :param id: The ID of the Organisation to be retrieved
    :type id: str

    :rtype: Organisation
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ORGANISATION_TYPE_URI,
        rdf_type_name=ORGANISATION_TYPE_NAME, 
        kls=Organisation)
