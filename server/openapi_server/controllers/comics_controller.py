import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import COMICS_TYPE_NAME, COMICS_TYPE_URI

from openapi_server.models.comics import Comics  # noqa: E501
from openapi_server import util

def comicss_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Comics

    Gets a list of all instances of Comics (more information in http://dbpedia.org/ontology/Comics) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Comics]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=COMICS_TYPE_URI,
        rdf_type_name=COMICS_TYPE_NAME, 
        kls=Comics)

def comicss_id_get(id):  # noqa: E501
    """Get a single Comics by its id

    Gets the details of a given Comics (more information in http://dbpedia.org/ontology/Comics) # noqa: E501

    :param id: The ID of the Comics to be retrieved
    :type id: str

    :rtype: Comics
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=COMICS_TYPE_URI,
        rdf_type_name=COMICS_TYPE_NAME, 
        kls=Comics)
