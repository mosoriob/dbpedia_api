import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import NONPROFITORGANISATION_TYPE_NAME, NONPROFITORGANISATION_TYPE_URI

from openapi_server.models.non_profit_organisation import NonProfitOrganisation  # noqa: E501
from openapi_server import util

def non_profitorganisations_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Non-ProfitOrganisation

    Gets a list of all instances of Non-ProfitOrganisation (more information in http://dbpedia.org/ontology/Non-ProfitOrganisation) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[NonProfitOrganisation]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=NONPROFITORGANISATION_TYPE_URI,
        rdf_type_name=NONPROFITORGANISATION_TYPE_NAME, 
        kls=NonProfitOrganisation)

def non_profitorganisations_id_get(id):  # noqa: E501
    """Get a single Non-ProfitOrganisation by its id

    Gets the details of a given Non-ProfitOrganisation (more information in http://dbpedia.org/ontology/Non-ProfitOrganisation) # noqa: E501

    :param id: The ID of the Non-ProfitOrganisation to be retrieved
    :type id: str

    :rtype: NonProfitOrganisation
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=NONPROFITORGANISATION_TYPE_URI,
        rdf_type_name=NONPROFITORGANISATION_TYPE_NAME, 
        kls=NonProfitOrganisation)
