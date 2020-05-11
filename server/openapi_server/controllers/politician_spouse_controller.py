import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import POLITICIANSPOUSE_TYPE_NAME, POLITICIANSPOUSE_TYPE_URI

from openapi_server.models.politician_spouse import PoliticianSpouse  # noqa: E501
from openapi_server import util

def politicianspouses_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of PoliticianSpouse

    Gets a list of all instances of PoliticianSpouse (more information in http://dbpedia.org/ontology/PoliticianSpouse) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[PoliticianSpouse]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=POLITICIANSPOUSE_TYPE_URI,
        rdf_type_name=POLITICIANSPOUSE_TYPE_NAME, 
        kls=PoliticianSpouse)

def politicianspouses_id_get(id):  # noqa: E501
    """Get a single PoliticianSpouse by its id

    Gets the details of a given PoliticianSpouse (more information in http://dbpedia.org/ontology/PoliticianSpouse) # noqa: E501

    :param id: The ID of the PoliticianSpouse to be retrieved
    :type id: str

    :rtype: PoliticianSpouse
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=POLITICIANSPOUSE_TYPE_URI,
        rdf_type_name=POLITICIANSPOUSE_TYPE_NAME, 
        kls=PoliticianSpouse)
