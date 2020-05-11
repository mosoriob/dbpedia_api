import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MEANOFTRANSPORTATION_TYPE_NAME, MEANOFTRANSPORTATION_TYPE_URI

from openapi_server.models.mean_of_transportation import MeanOfTransportation  # noqa: E501
from openapi_server import util

def meanoftransportations_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of MeanOfTransportation

    Gets a list of all instances of MeanOfTransportation (more information in http://dbpedia.org/ontology/MeanOfTransportation) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[MeanOfTransportation]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MEANOFTRANSPORTATION_TYPE_URI,
        rdf_type_name=MEANOFTRANSPORTATION_TYPE_NAME, 
        kls=MeanOfTransportation)

def meanoftransportations_id_get(id):  # noqa: E501
    """Get a single MeanOfTransportation by its id

    Gets the details of a given MeanOfTransportation (more information in http://dbpedia.org/ontology/MeanOfTransportation) # noqa: E501

    :param id: The ID of the MeanOfTransportation to be retrieved
    :type id: str

    :rtype: MeanOfTransportation
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MEANOFTRANSPORTATION_TYPE_URI,
        rdf_type_name=MEANOFTRANSPORTATION_TYPE_NAME, 
        kls=MeanOfTransportation)
