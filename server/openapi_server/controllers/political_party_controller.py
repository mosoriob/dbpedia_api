import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import POLITICALPARTY_TYPE_NAME, POLITICALPARTY_TYPE_URI

from openapi_server.models.political_party import PoliticalParty  # noqa: E501
from openapi_server import util

def politicalpartys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of PoliticalParty

    Gets a list of all instances of PoliticalParty (more information in http://dbpedia.org/ontology/PoliticalParty) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[PoliticalParty]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=POLITICALPARTY_TYPE_URI,
        rdf_type_name=POLITICALPARTY_TYPE_NAME, 
        kls=PoliticalParty)

def politicalpartys_id_get(id):  # noqa: E501
    """Get a single PoliticalParty by its id

    Gets the details of a given PoliticalParty (more information in http://dbpedia.org/ontology/PoliticalParty) # noqa: E501

    :param id: The ID of the PoliticalParty to be retrieved
    :type id: str

    :rtype: PoliticalParty
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=POLITICALPARTY_TYPE_URI,
        rdf_type_name=POLITICALPARTY_TYPE_NAME, 
        kls=PoliticalParty)
