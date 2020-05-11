import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import RACEHORSE_TYPE_NAME, RACEHORSE_TYPE_URI

from openapi_server.models.race_horse import RaceHorse  # noqa: E501
from openapi_server import util

def racehorses_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of RaceHorse

    Gets a list of all instances of RaceHorse (more information in http://dbpedia.org/ontology/RaceHorse) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[RaceHorse]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=RACEHORSE_TYPE_URI,
        rdf_type_name=RACEHORSE_TYPE_NAME, 
        kls=RaceHorse)

def racehorses_id_get(id):  # noqa: E501
    """Get a single RaceHorse by its id

    Gets the details of a given RaceHorse (more information in http://dbpedia.org/ontology/RaceHorse) # noqa: E501

    :param id: The ID of the RaceHorse to be retrieved
    :type id: str

    :rtype: RaceHorse
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=RACEHORSE_TYPE_URI,
        rdf_type_name=RACEHORSE_TYPE_NAME, 
        kls=RaceHorse)
