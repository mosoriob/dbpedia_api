import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MILITARYSTRUCTURE_TYPE_NAME, MILITARYSTRUCTURE_TYPE_URI

from openapi_server.models.military_structure import MilitaryStructure  # noqa: E501
from openapi_server import util

def militarystructures_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of MilitaryStructure

    Gets a list of all instances of MilitaryStructure (more information in http://dbpedia.org/ontology/MilitaryStructure) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[MilitaryStructure]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MILITARYSTRUCTURE_TYPE_URI,
        rdf_type_name=MILITARYSTRUCTURE_TYPE_NAME, 
        kls=MilitaryStructure)

def militarystructures_id_get(id):  # noqa: E501
    """Get a single MilitaryStructure by its id

    Gets the details of a given MilitaryStructure (more information in http://dbpedia.org/ontology/MilitaryStructure) # noqa: E501

    :param id: The ID of the MilitaryStructure to be retrieved
    :type id: str

    :rtype: MilitaryStructure
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MILITARYSTRUCTURE_TYPE_URI,
        rdf_type_name=MILITARYSTRUCTURE_TYPE_NAME, 
        kls=MilitaryStructure)
