import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import IMDB_TYPE_NAME, IMDB_TYPE_URI

from openapi_server.models.imdb import Imdb  # noqa: E501
from openapi_server import util

def imdbs_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Imdb

    Gets a list of all instances of Imdb (more information in http://dbpedia.org/ontology/Imdb) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Imdb]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=IMDB_TYPE_URI,
        rdf_type_name=IMDB_TYPE_NAME, 
        kls=Imdb)

def imdbs_id_get(id):  # noqa: E501
    """Get a single Imdb by its id

    Gets the details of a given Imdb (more information in http://dbpedia.org/ontology/Imdb) # noqa: E501

    :param id: The ID of the Imdb to be retrieved
    :type id: str

    :rtype: Imdb
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=IMDB_TYPE_URI,
        rdf_type_name=IMDB_TYPE_NAME, 
        kls=Imdb)
