import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import FUNGUS_TYPE_NAME, FUNGUS_TYPE_URI

from openapi_server.models.fungus import Fungus  # noqa: E501
from openapi_server import util

def funguss_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Fungus

    Gets a list of all instances of Fungus (more information in http://dbpedia.org/ontology/Fungus) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Fungus]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=FUNGUS_TYPE_URI,
        rdf_type_name=FUNGUS_TYPE_NAME, 
        kls=Fungus)

def funguss_id_get(id):  # noqa: E501
    """Get a single Fungus by its id

    Gets the details of a given Fungus (more information in http://dbpedia.org/ontology/Fungus) # noqa: E501

    :param id: The ID of the Fungus to be retrieved
    :type id: str

    :rtype: Fungus
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=FUNGUS_TYPE_URI,
        rdf_type_name=FUNGUS_TYPE_NAME, 
        kls=Fungus)
