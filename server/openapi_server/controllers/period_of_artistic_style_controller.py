import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PERIODOFARTISTICSTYLE_TYPE_NAME, PERIODOFARTISTICSTYLE_TYPE_URI

from openapi_server.models.period_of_artistic_style import PeriodOfArtisticStyle  # noqa: E501
from openapi_server import util

def periodofartisticstyles_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of PeriodOfArtisticStyle

    Gets a list of all instances of PeriodOfArtisticStyle (more information in http://dbpedia.org/ontology/PeriodOfArtisticStyle) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[PeriodOfArtisticStyle]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PERIODOFARTISTICSTYLE_TYPE_URI,
        rdf_type_name=PERIODOFARTISTICSTYLE_TYPE_NAME, 
        kls=PeriodOfArtisticStyle)

def periodofartisticstyles_id_get(id):  # noqa: E501
    """Get a single PeriodOfArtisticStyle by its id

    Gets the details of a given PeriodOfArtisticStyle (more information in http://dbpedia.org/ontology/PeriodOfArtisticStyle) # noqa: E501

    :param id: The ID of the PeriodOfArtisticStyle to be retrieved
    :type id: str

    :rtype: PeriodOfArtisticStyle
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PERIODOFARTISTICSTYLE_TYPE_URI,
        rdf_type_name=PERIODOFARTISTICSTYLE_TYPE_NAME, 
        kls=PeriodOfArtisticStyle)
