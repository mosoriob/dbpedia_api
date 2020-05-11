import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import NATIONALCOLLEGIATEATHLETICASSOCIATIONATHLETE_TYPE_NAME, NATIONALCOLLEGIATEATHLETICASSOCIATIONATHLETE_TYPE_URI

from openapi_server.models.national_collegiate_athletic_association_athlete import NationalCollegiateAthleticAssociationAthlete  # noqa: E501
from openapi_server import util

def nationalcollegiateathleticassociationathletes_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of NationalCollegiateAthleticAssociationAthlete

    Gets a list of all instances of NationalCollegiateAthleticAssociationAthlete (more information in http://dbpedia.org/ontology/NationalCollegiateAthleticAssociationAthlete) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[NationalCollegiateAthleticAssociationAthlete]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=NATIONALCOLLEGIATEATHLETICASSOCIATIONATHLETE_TYPE_URI,
        rdf_type_name=NATIONALCOLLEGIATEATHLETICASSOCIATIONATHLETE_TYPE_NAME, 
        kls=NationalCollegiateAthleticAssociationAthlete)

def nationalcollegiateathleticassociationathletes_id_get(id):  # noqa: E501
    """Get a single NationalCollegiateAthleticAssociationAthlete by its id

    Gets the details of a given NationalCollegiateAthleticAssociationAthlete (more information in http://dbpedia.org/ontology/NationalCollegiateAthleticAssociationAthlete) # noqa: E501

    :param id: The ID of the NationalCollegiateAthleticAssociationAthlete to be retrieved
    :type id: str

    :rtype: NationalCollegiateAthleticAssociationAthlete
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=NATIONALCOLLEGIATEATHLETICASSOCIATIONATHLETE_TYPE_URI,
        rdf_type_name=NATIONALCOLLEGIATEATHLETICASSOCIATIONATHLETE_TYPE_NAME, 
        kls=NationalCollegiateAthleticAssociationAthlete)
