import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MANHWA_TYPE_NAME, MANHWA_TYPE_URI

from openapi_server.models.manhwa import Manhwa  # noqa: E501
from openapi_server import util

def manhwas_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Manhwa

    Gets a list of all instances of Manhwa (more information in http://dbpedia.org/ontology/Manhwa) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Manhwa]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MANHWA_TYPE_URI,
        rdf_type_name=MANHWA_TYPE_NAME, 
        kls=Manhwa)

def manhwas_id_get(id):  # noqa: E501
    """Get a single Manhwa by its id

    Gets the details of a given Manhwa (more information in http://dbpedia.org/ontology/Manhwa) # noqa: E501

    :param id: The ID of the Manhwa to be retrieved
    :type id: str

    :rtype: Manhwa
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MANHWA_TYPE_URI,
        rdf_type_name=MANHWA_TYPE_NAME, 
        kls=Manhwa)
