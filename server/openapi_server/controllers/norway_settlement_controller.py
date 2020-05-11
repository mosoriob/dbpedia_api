import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import NORWAYSETTLEMENT_TYPE_NAME, NORWAYSETTLEMENT_TYPE_URI

from openapi_server.models.norway_settlement import NorwaySettlement  # noqa: E501
from openapi_server import util

def norwaysettlements_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of NorwaySettlement

    Gets a list of all instances of NorwaySettlement (more information in http://dbpedia.org/ontology/NorwaySettlement) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[NorwaySettlement]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=NORWAYSETTLEMENT_TYPE_URI,
        rdf_type_name=NORWAYSETTLEMENT_TYPE_NAME, 
        kls=NorwaySettlement)

def norwaysettlements_id_get(id):  # noqa: E501
    """Get a single NorwaySettlement by its id

    Gets the details of a given NorwaySettlement (more information in http://dbpedia.org/ontology/NorwaySettlement) # noqa: E501

    :param id: The ID of the NorwaySettlement to be retrieved
    :type id: str

    :rtype: NorwaySettlement
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=NORWAYSETTLEMENT_TYPE_URI,
        rdf_type_name=NORWAYSETTLEMENT_TYPE_NAME, 
        kls=NorwaySettlement)
