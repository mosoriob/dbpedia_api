import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MOTORSPORTSEASON_TYPE_NAME, MOTORSPORTSEASON_TYPE_URI

from openapi_server.models.motorsport_season import MotorsportSeason  # noqa: E501
from openapi_server import util

def motorsportseasons_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of MotorsportSeason

    Gets a list of all instances of MotorsportSeason (more information in http://dbpedia.org/ontology/MotorsportSeason) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[MotorsportSeason]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MOTORSPORTSEASON_TYPE_URI,
        rdf_type_name=MOTORSPORTSEASON_TYPE_NAME, 
        kls=MotorsportSeason)

def motorsportseasons_id_get(id):  # noqa: E501
    """Get a single MotorsportSeason by its id

    Gets the details of a given MotorsportSeason (more information in http://dbpedia.org/ontology/MotorsportSeason) # noqa: E501

    :param id: The ID of the MotorsportSeason to be retrieved
    :type id: str

    :rtype: MotorsportSeason
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MOTORSPORTSEASON_TYPE_URI,
        rdf_type_name=MOTORSPORTSEASON_TYPE_NAME, 
        kls=MotorsportSeason)
