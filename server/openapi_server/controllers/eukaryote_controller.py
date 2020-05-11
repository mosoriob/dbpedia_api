import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import EUKARYOTE_TYPE_NAME, EUKARYOTE_TYPE_URI

from openapi_server.models.eukaryote import Eukaryote  # noqa: E501
from openapi_server import util

def eukaryotes_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Eukaryote

    Gets a list of all instances of Eukaryote (more information in http://dbpedia.org/ontology/Eukaryote) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Eukaryote]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=EUKARYOTE_TYPE_URI,
        rdf_type_name=EUKARYOTE_TYPE_NAME, 
        kls=Eukaryote)

def eukaryotes_id_get(id):  # noqa: E501
    """Get a single Eukaryote by its id

    Gets the details of a given Eukaryote (more information in http://dbpedia.org/ontology/Eukaryote) # noqa: E501

    :param id: The ID of the Eukaryote to be retrieved
    :type id: str

    :rtype: Eukaryote
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=EUKARYOTE_TYPE_URI,
        rdf_type_name=EUKARYOTE_TYPE_NAME, 
        kls=Eukaryote)
