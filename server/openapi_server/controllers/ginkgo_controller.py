import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GINKGO_TYPE_NAME, GINKGO_TYPE_URI

from openapi_server.models.ginkgo import Ginkgo  # noqa: E501
from openapi_server import util

def ginkgos_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Ginkgo

    Gets a list of all instances of Ginkgo (more information in http://dbpedia.org/ontology/Ginkgo) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Ginkgo]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GINKGO_TYPE_URI,
        rdf_type_name=GINKGO_TYPE_NAME, 
        kls=Ginkgo)

def ginkgos_id_get(id):  # noqa: E501
    """Get a single Ginkgo by its id

    Gets the details of a given Ginkgo (more information in http://dbpedia.org/ontology/Ginkgo) # noqa: E501

    :param id: The ID of the Ginkgo to be retrieved
    :type id: str

    :rtype: Ginkgo
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GINKGO_TYPE_URI,
        rdf_type_name=GINKGO_TYPE_NAME, 
        kls=Ginkgo)
