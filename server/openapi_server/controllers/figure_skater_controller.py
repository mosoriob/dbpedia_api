import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import FIGURESKATER_TYPE_NAME, FIGURESKATER_TYPE_URI

from openapi_server.models.figure_skater import FigureSkater  # noqa: E501
from openapi_server import util

def figureskaters_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of FigureSkater

    Gets a list of all instances of FigureSkater (more information in http://dbpedia.org/ontology/FigureSkater) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[FigureSkater]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=FIGURESKATER_TYPE_URI,
        rdf_type_name=FIGURESKATER_TYPE_NAME, 
        kls=FigureSkater)

def figureskaters_id_get(id):  # noqa: E501
    """Get a single FigureSkater by its id

    Gets the details of a given FigureSkater (more information in http://dbpedia.org/ontology/FigureSkater) # noqa: E501

    :param id: The ID of the FigureSkater to be retrieved
    :type id: str

    :rtype: FigureSkater
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=FIGURESKATER_TYPE_URI,
        rdf_type_name=FIGURESKATER_TYPE_NAME, 
        kls=FigureSkater)
