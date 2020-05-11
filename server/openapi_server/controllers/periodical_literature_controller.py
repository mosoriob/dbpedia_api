import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PERIODICALLITERATURE_TYPE_NAME, PERIODICALLITERATURE_TYPE_URI

from openapi_server.models.periodical_literature import PeriodicalLiterature  # noqa: E501
from openapi_server import util

def periodicalliteratures_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of PeriodicalLiterature

    Gets a list of all instances of PeriodicalLiterature (more information in http://dbpedia.org/ontology/PeriodicalLiterature) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[PeriodicalLiterature]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PERIODICALLITERATURE_TYPE_URI,
        rdf_type_name=PERIODICALLITERATURE_TYPE_NAME, 
        kls=PeriodicalLiterature)

def periodicalliteratures_id_get(id):  # noqa: E501
    """Get a single PeriodicalLiterature by its id

    Gets the details of a given PeriodicalLiterature (more information in http://dbpedia.org/ontology/PeriodicalLiterature) # noqa: E501

    :param id: The ID of the PeriodicalLiterature to be retrieved
    :type id: str

    :rtype: PeriodicalLiterature
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PERIODICALLITERATURE_TYPE_URI,
        rdf_type_name=PERIODICALLITERATURE_TYPE_NAME, 
        kls=PeriodicalLiterature)
