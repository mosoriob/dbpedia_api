import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SKYSCRAPER_TYPE_NAME, SKYSCRAPER_TYPE_URI

from openapi_server.models.skyscraper import Skyscraper  # noqa: E501
from openapi_server import util

def skyscrapers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Skyscraper

    Gets a list of all instances of Skyscraper (more information in http://dbpedia.org/ontology/Skyscraper) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Skyscraper]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SKYSCRAPER_TYPE_URI,
        rdf_type_name=SKYSCRAPER_TYPE_NAME, 
        kls=Skyscraper)

def skyscrapers_id_get(id):  # noqa: E501
    """Get a single Skyscraper by its id

    Gets the details of a given Skyscraper (more information in http://dbpedia.org/ontology/Skyscraper) # noqa: E501

    :param id: The ID of the Skyscraper to be retrieved
    :type id: str

    :rtype: Skyscraper
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SKYSCRAPER_TYPE_URI,
        rdf_type_name=SKYSCRAPER_TYPE_NAME, 
        kls=Skyscraper)
