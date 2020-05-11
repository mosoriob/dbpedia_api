import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import NUCLEARPOWERSTATION_TYPE_NAME, NUCLEARPOWERSTATION_TYPE_URI

from openapi_server.models.nuclear_power_station import NuclearPowerStation  # noqa: E501
from openapi_server import util

def nuclearpowerstations_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of NuclearPowerStation

    Gets a list of all instances of NuclearPowerStation (more information in http://dbpedia.org/ontology/NuclearPowerStation) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[NuclearPowerStation]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=NUCLEARPOWERSTATION_TYPE_URI,
        rdf_type_name=NUCLEARPOWERSTATION_TYPE_NAME, 
        kls=NuclearPowerStation)

def nuclearpowerstations_id_get(id):  # noqa: E501
    """Get a single NuclearPowerStation by its id

    Gets the details of a given NuclearPowerStation (more information in http://dbpedia.org/ontology/NuclearPowerStation) # noqa: E501

    :param id: The ID of the NuclearPowerStation to be retrieved
    :type id: str

    :rtype: NuclearPowerStation
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=NUCLEARPOWERSTATION_TYPE_URI,
        rdf_type_name=NUCLEARPOWERSTATION_TYPE_NAME, 
        kls=NuclearPowerStation)
