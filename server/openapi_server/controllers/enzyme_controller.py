import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ENZYME_TYPE_NAME, ENZYME_TYPE_URI

from openapi_server.models.enzyme import Enzyme  # noqa: E501
from openapi_server import util

def enzymes_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Enzyme

    Gets a list of all instances of Enzyme (more information in http://dbpedia.org/ontology/Enzyme) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Enzyme]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ENZYME_TYPE_URI,
        rdf_type_name=ENZYME_TYPE_NAME, 
        kls=Enzyme)

def enzymes_id_get(id):  # noqa: E501
    """Get a single Enzyme by its id

    Gets the details of a given Enzyme (more information in http://dbpedia.org/ontology/Enzyme) # noqa: E501

    :param id: The ID of the Enzyme to be retrieved
    :type id: str

    :rtype: Enzyme
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ENZYME_TYPE_URI,
        rdf_type_name=ENZYME_TYPE_NAME, 
        kls=Enzyme)
