import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CULTIVATEDVARIETY_TYPE_NAME, CULTIVATEDVARIETY_TYPE_URI

from openapi_server.models.cultivated_variety import CultivatedVariety  # noqa: E501
from openapi_server import util

def cultivatedvarietys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of CultivatedVariety

    Gets a list of all instances of CultivatedVariety (more information in http://dbpedia.org/ontology/CultivatedVariety) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[CultivatedVariety]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CULTIVATEDVARIETY_TYPE_URI,
        rdf_type_name=CULTIVATEDVARIETY_TYPE_NAME, 
        kls=CultivatedVariety)

def cultivatedvarietys_id_get(id):  # noqa: E501
    """Get a single CultivatedVariety by its id

    Gets the details of a given CultivatedVariety (more information in http://dbpedia.org/ontology/CultivatedVariety) # noqa: E501

    :param id: The ID of the CultivatedVariety to be retrieved
    :type id: str

    :rtype: CultivatedVariety
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CULTIVATEDVARIETY_TYPE_URI,
        rdf_type_name=CULTIVATEDVARIETY_TYPE_NAME, 
        kls=CultivatedVariety)
