import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ECONOMIST_TYPE_NAME, ECONOMIST_TYPE_URI

from openapi_server.models.economist import Economist  # noqa: E501
from openapi_server import util

def economists_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Economist

    Gets a list of all instances of Economist (more information in http://dbpedia.org/ontology/Economist) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Economist]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ECONOMIST_TYPE_URI,
        rdf_type_name=ECONOMIST_TYPE_NAME, 
        kls=Economist)

def economists_id_get(id):  # noqa: E501
    """Get a single Economist by its id

    Gets the details of a given Economist (more information in http://dbpedia.org/ontology/Economist) # noqa: E501

    :param id: The ID of the Economist to be retrieved
    :type id: str

    :rtype: Economist
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ECONOMIST_TYPE_URI,
        rdf_type_name=ECONOMIST_TYPE_NAME, 
        kls=Economist)
