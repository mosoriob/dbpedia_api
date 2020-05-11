import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ADULTACTOR_TYPE_NAME, ADULTACTOR_TYPE_URI

from openapi_server.models.adult_actor import AdultActor  # noqa: E501
from openapi_server import util

def adultactors_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of AdultActor

    Gets a list of all instances of AdultActor (more information in http://dbpedia.org/ontology/AdultActor) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[AdultActor]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ADULTACTOR_TYPE_URI,
        rdf_type_name=ADULTACTOR_TYPE_NAME, 
        kls=AdultActor)

def adultactors_id_get(id):  # noqa: E501
    """Get a single AdultActor by its id

    Gets the details of a given AdultActor (more information in http://dbpedia.org/ontology/AdultActor) # noqa: E501

    :param id: The ID of the AdultActor to be retrieved
    :type id: str

    :rtype: AdultActor
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ADULTACTOR_TYPE_URI,
        rdf_type_name=ADULTACTOR_TYPE_NAME, 
        kls=AdultActor)
