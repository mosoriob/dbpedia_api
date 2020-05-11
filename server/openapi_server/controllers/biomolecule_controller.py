import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BIOMOLECULE_TYPE_NAME, BIOMOLECULE_TYPE_URI

from openapi_server.models.biomolecule import Biomolecule  # noqa: E501
from openapi_server import util

def biomolecules_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Biomolecule

    Gets a list of all instances of Biomolecule (more information in http://dbpedia.org/ontology/Biomolecule) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Biomolecule]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BIOMOLECULE_TYPE_URI,
        rdf_type_name=BIOMOLECULE_TYPE_NAME, 
        kls=Biomolecule)

def biomolecules_id_get(id):  # noqa: E501
    """Get a single Biomolecule by its id

    Gets the details of a given Biomolecule (more information in http://dbpedia.org/ontology/Biomolecule) # noqa: E501

    :param id: The ID of the Biomolecule to be retrieved
    :type id: str

    :rtype: Biomolecule
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BIOMOLECULE_TYPE_URI,
        rdf_type_name=BIOMOLECULE_TYPE_NAME, 
        kls=Biomolecule)
