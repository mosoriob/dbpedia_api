import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import POLYHEDRON_TYPE_NAME, POLYHEDRON_TYPE_URI

from openapi_server.models.polyhedron import Polyhedron  # noqa: E501
from openapi_server import util

def polyhedrons_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Polyhedron

    Gets a list of all instances of Polyhedron (more information in http://dbpedia.org/ontology/Polyhedron) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Polyhedron]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=POLYHEDRON_TYPE_URI,
        rdf_type_name=POLYHEDRON_TYPE_NAME, 
        kls=Polyhedron)

def polyhedrons_id_get(id):  # noqa: E501
    """Get a single Polyhedron by its id

    Gets the details of a given Polyhedron (more information in http://dbpedia.org/ontology/Polyhedron) # noqa: E501

    :param id: The ID of the Polyhedron to be retrieved
    :type id: str

    :rtype: Polyhedron
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=POLYHEDRON_TYPE_URI,
        rdf_type_name=POLYHEDRON_TYPE_NAME, 
        kls=Polyhedron)
