import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import RAILWAYLINE_TYPE_NAME, RAILWAYLINE_TYPE_URI

from openapi_server.models.railway_line import RailwayLine  # noqa: E501
from openapi_server import util

def railwaylines_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of RailwayLine

    Gets a list of all instances of RailwayLine (more information in http://dbpedia.org/ontology/RailwayLine) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[RailwayLine]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=RAILWAYLINE_TYPE_URI,
        rdf_type_name=RAILWAYLINE_TYPE_NAME, 
        kls=RailwayLine)

def railwaylines_id_get(id):  # noqa: E501
    """Get a single RailwayLine by its id

    Gets the details of a given RailwayLine (more information in http://dbpedia.org/ontology/RailwayLine) # noqa: E501

    :param id: The ID of the RailwayLine to be retrieved
    :type id: str

    :rtype: RailwayLine
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=RAILWAYLINE_TYPE_URI,
        rdf_type_name=RAILWAYLINE_TYPE_NAME, 
        kls=RailwayLine)
