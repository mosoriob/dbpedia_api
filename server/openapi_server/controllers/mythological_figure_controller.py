import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MYTHOLOGICALFIGURE_TYPE_NAME, MYTHOLOGICALFIGURE_TYPE_URI

from openapi_server.models.mythological_figure import MythologicalFigure  # noqa: E501
from openapi_server import util

def mythologicalfigures_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of MythologicalFigure

    Gets a list of all instances of MythologicalFigure (more information in http://dbpedia.org/ontology/MythologicalFigure) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[MythologicalFigure]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MYTHOLOGICALFIGURE_TYPE_URI,
        rdf_type_name=MYTHOLOGICALFIGURE_TYPE_NAME, 
        kls=MythologicalFigure)

def mythologicalfigures_id_get(id):  # noqa: E501
    """Get a single MythologicalFigure by its id

    Gets the details of a given MythologicalFigure (more information in http://dbpedia.org/ontology/MythologicalFigure) # noqa: E501

    :param id: The ID of the MythologicalFigure to be retrieved
    :type id: str

    :rtype: MythologicalFigure
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MYTHOLOGICALFIGURE_TYPE_URI,
        rdf_type_name=MYTHOLOGICALFIGURE_TYPE_NAME, 
        kls=MythologicalFigure)
