import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CHARTSPLACEMENTS_TYPE_NAME, CHARTSPLACEMENTS_TYPE_URI

from openapi_server.models.charts_placements import ChartsPlacements  # noqa: E501
from openapi_server import util

def chartsplacementss_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of ChartsPlacements

    Gets a list of all instances of ChartsPlacements (more information in http://dbpedia.org/ontology/ChartsPlacements) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[ChartsPlacements]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CHARTSPLACEMENTS_TYPE_URI,
        rdf_type_name=CHARTSPLACEMENTS_TYPE_NAME, 
        kls=ChartsPlacements)

def chartsplacementss_id_get(id):  # noqa: E501
    """Get a single ChartsPlacements by its id

    Gets the details of a given ChartsPlacements (more information in http://dbpedia.org/ontology/ChartsPlacements) # noqa: E501

    :param id: The ID of the ChartsPlacements to be retrieved
    :type id: str

    :rtype: ChartsPlacements
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CHARTSPLACEMENTS_TYPE_URI,
        rdf_type_name=CHARTSPLACEMENTS_TYPE_NAME, 
        kls=ChartsPlacements)
