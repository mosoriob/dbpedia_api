import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import COUNTRYSEAT_TYPE_NAME, COUNTRYSEAT_TYPE_URI

from openapi_server.models.country_seat import CountrySeat  # noqa: E501
from openapi_server import util

def countryseats_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of CountrySeat

    Gets a list of all instances of CountrySeat (more information in http://dbpedia.org/ontology/CountrySeat) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[CountrySeat]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=COUNTRYSEAT_TYPE_URI,
        rdf_type_name=COUNTRYSEAT_TYPE_NAME, 
        kls=CountrySeat)

def countryseats_id_get(id):  # noqa: E501
    """Get a single CountrySeat by its id

    Gets the details of a given CountrySeat (more information in http://dbpedia.org/ontology/CountrySeat) # noqa: E501

    :param id: The ID of the CountrySeat to be retrieved
    :type id: str

    :rtype: CountrySeat
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=COUNTRYSEAT_TYPE_URI,
        rdf_type_name=COUNTRYSEAT_TYPE_NAME, 
        kls=CountrySeat)
