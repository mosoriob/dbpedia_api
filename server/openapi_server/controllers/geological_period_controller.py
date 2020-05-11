import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GEOLOGICALPERIOD_TYPE_NAME, GEOLOGICALPERIOD_TYPE_URI

from openapi_server.models.geological_period import GeologicalPeriod  # noqa: E501
from openapi_server import util

def geologicalperiods_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of GeologicalPeriod

    Gets a list of all instances of GeologicalPeriod (more information in http://dbpedia.org/ontology/GeologicalPeriod) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[GeologicalPeriod]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GEOLOGICALPERIOD_TYPE_URI,
        rdf_type_name=GEOLOGICALPERIOD_TYPE_NAME, 
        kls=GeologicalPeriod)

def geologicalperiods_id_get(id):  # noqa: E501
    """Get a single GeologicalPeriod by its id

    Gets the details of a given GeologicalPeriod (more information in http://dbpedia.org/ontology/GeologicalPeriod) # noqa: E501

    :param id: The ID of the GeologicalPeriod to be retrieved
    :type id: str

    :rtype: GeologicalPeriod
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GEOLOGICALPERIOD_TYPE_URI,
        rdf_type_name=GEOLOGICALPERIOD_TYPE_NAME, 
        kls=GeologicalPeriod)
