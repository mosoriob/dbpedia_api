import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import RECORDLABEL_TYPE_NAME, RECORDLABEL_TYPE_URI

from openapi_server.models.record_label import RecordLabel  # noqa: E501
from openapi_server import util

def recordlabels_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of RecordLabel

    Gets a list of all instances of RecordLabel (more information in http://dbpedia.org/ontology/RecordLabel) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[RecordLabel]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=RECORDLABEL_TYPE_URI,
        rdf_type_name=RECORDLABEL_TYPE_NAME, 
        kls=RecordLabel)

def recordlabels_id_get(id):  # noqa: E501
    """Get a single RecordLabel by its id

    Gets the details of a given RecordLabel (more information in http://dbpedia.org/ontology/RecordLabel) # noqa: E501

    :param id: The ID of the RecordLabel to be retrieved
    :type id: str

    :rtype: RecordLabel
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=RECORDLABEL_TYPE_URI,
        rdf_type_name=RECORDLABEL_TYPE_NAME, 
        kls=RecordLabel)
