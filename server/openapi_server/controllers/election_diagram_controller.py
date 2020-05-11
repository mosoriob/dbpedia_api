import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ELECTIONDIAGRAM_TYPE_NAME, ELECTIONDIAGRAM_TYPE_URI

from openapi_server.models.election_diagram import ElectionDiagram  # noqa: E501
from openapi_server import util

def electiondiagrams_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of ElectionDiagram

    Gets a list of all instances of ElectionDiagram (more information in http://dbpedia.org/ontology/ElectionDiagram) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[ElectionDiagram]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ELECTIONDIAGRAM_TYPE_URI,
        rdf_type_name=ELECTIONDIAGRAM_TYPE_NAME, 
        kls=ElectionDiagram)

def electiondiagrams_id_get(id):  # noqa: E501
    """Get a single ElectionDiagram by its id

    Gets the details of a given ElectionDiagram (more information in http://dbpedia.org/ontology/ElectionDiagram) # noqa: E501

    :param id: The ID of the ElectionDiagram to be retrieved
    :type id: str

    :rtype: ElectionDiagram
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ELECTIONDIAGRAM_TYPE_URI,
        rdf_type_name=ELECTIONDIAGRAM_TYPE_NAME, 
        kls=ElectionDiagram)
