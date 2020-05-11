import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CITYDISTRICT_TYPE_NAME, CITYDISTRICT_TYPE_URI

from openapi_server.models.city_district import CityDistrict  # noqa: E501
from openapi_server import util

def citydistricts_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of CityDistrict

    Gets a list of all instances of CityDistrict (more information in http://dbpedia.org/ontology/CityDistrict) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[CityDistrict]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CITYDISTRICT_TYPE_URI,
        rdf_type_name=CITYDISTRICT_TYPE_NAME, 
        kls=CityDistrict)

def citydistricts_id_get(id):  # noqa: E501
    """Get a single CityDistrict by its id

    Gets the details of a given CityDistrict (more information in http://dbpedia.org/ontology/CityDistrict) # noqa: E501

    :param id: The ID of the CityDistrict to be retrieved
    :type id: str

    :rtype: CityDistrict
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CITYDISTRICT_TYPE_URI,
        rdf_type_name=CITYDISTRICT_TYPE_NAME, 
        kls=CityDistrict)
