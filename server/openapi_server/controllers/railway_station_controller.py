import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import RAILWAYSTATION_TYPE_NAME, RAILWAYSTATION_TYPE_URI

from openapi_server.models.railway_station import RailwayStation  # noqa: E501
from openapi_server import util

def railwaystations_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of RailwayStation

    Gets a list of all instances of RailwayStation (more information in http://dbpedia.org/ontology/RailwayStation) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[RailwayStation]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=RAILWAYSTATION_TYPE_URI,
        rdf_type_name=RAILWAYSTATION_TYPE_NAME, 
        kls=RailwayStation)

def railwaystations_id_get(id):  # noqa: E501
    """Get a single RailwayStation by its id

    Gets the details of a given RailwayStation (more information in http://dbpedia.org/ontology/RailwayStation) # noqa: E501

    :param id: The ID of the RailwayStation to be retrieved
    :type id: str

    :rtype: RailwayStation
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=RAILWAYSTATION_TYPE_URI,
        rdf_type_name=RAILWAYSTATION_TYPE_NAME, 
        kls=RailwayStation)
