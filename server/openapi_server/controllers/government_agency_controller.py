import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GOVERNMENTAGENCY_TYPE_NAME, GOVERNMENTAGENCY_TYPE_URI

from openapi_server.models.government_agency import GovernmentAgency  # noqa: E501
from openapi_server import util

def governmentagencys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of GovernmentAgency

    Gets a list of all instances of GovernmentAgency (more information in http://dbpedia.org/ontology/GovernmentAgency) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[GovernmentAgency]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GOVERNMENTAGENCY_TYPE_URI,
        rdf_type_name=GOVERNMENTAGENCY_TYPE_NAME, 
        kls=GovernmentAgency)

def governmentagencys_id_get(id):  # noqa: E501
    """Get a single GovernmentAgency by its id

    Gets the details of a given GovernmentAgency (more information in http://dbpedia.org/ontology/GovernmentAgency) # noqa: E501

    :param id: The ID of the GovernmentAgency to be retrieved
    :type id: str

    :rtype: GovernmentAgency
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GOVERNMENTAGENCY_TYPE_URI,
        rdf_type_name=GOVERNMENTAGENCY_TYPE_NAME, 
        kls=GovernmentAgency)
