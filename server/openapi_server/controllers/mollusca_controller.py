import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MOLLUSCA_TYPE_NAME, MOLLUSCA_TYPE_URI

from openapi_server.models.mollusca import Mollusca  # noqa: E501
from openapi_server import util

def molluscas_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Mollusca

    Gets a list of all instances of Mollusca (more information in http://dbpedia.org/ontology/Mollusca) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Mollusca]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MOLLUSCA_TYPE_URI,
        rdf_type_name=MOLLUSCA_TYPE_NAME, 
        kls=Mollusca)

def molluscas_id_get(id):  # noqa: E501
    """Get a single Mollusca by its id

    Gets the details of a given Mollusca (more information in http://dbpedia.org/ontology/Mollusca) # noqa: E501

    :param id: The ID of the Mollusca to be retrieved
    :type id: str

    :rtype: Mollusca
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MOLLUSCA_TYPE_URI,
        rdf_type_name=MOLLUSCA_TYPE_NAME, 
        kls=Mollusca)
