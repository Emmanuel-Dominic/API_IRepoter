"""views file for create, edit, get and delete redflad incidents"""
from flask import Blueprint, jsonify, request, Response, json
from models.incident import Incident


incident_bp = Blueprint('incident_bp', __name__, url_prefix='/api/v1')

incidents_db = [
    Incident(
        location={"location_long":"0.39737", "location_lat":"9.38974"},
        createdOn="2018-11-25 22:41:14",
        createdBy="2",
        type='redflag',
        # status="under_Investigation",
        images="1.jpeg",
        videos="1.gif",
        comment="Arnold was caught stilling jack fruit in hassan's Garden"
        ),
    Incident(
        location={"location_long":"0.33737", "location_lat":"5.38974"},
        createdOn="2018-08-24 02:31:14",
        createdBy="2",
        type='intervention',
        # status="resolved",
        images="2.jpeg",
        videos="2.gif",
        comment="Malamba highway needs construction because it's in bad state and it's also causing alot of accidents"
        ),
    Incident(
        location={"location_long":"0.39737", "location_lat":"9.38974"},
        createdOn="2018-11-25 22:41:14",
        createdBy="2",
        type='redflag',
        # status="rejected",
        images="3.jpeg",
        videos="3.gif",
        comment="Hussien knocked moses's cow along masaka road, he was drank"
        )
        ]


@incident_bp.route('/redflags', methods=['GET'])
def get_all_redflags():
    """docstring function that return all redflags detials"""
    redflags_list = []
    for record in incidents_db:
        if record['type'] == redflag:
            redflags_list.append(redflag.get_incident_details())
            return jsonify({
                "status": 200,
                "data": redflags_list['type']
            }), 200
        return jsonify({
            "status": 404,
            "error": "bad request"
        }), 200

@incident_bp.route('/red-flags/<int:redFlagId>', methods=['GET'])
def get_specific_redflag(redFlagId):
    for record in incidents_db:
        if record['type'] == redflag:
            if record['incidentId'] == redFlagId:
                return jsonify({
                    "status": 200,
                    "data": record
                }), 200
            return jsonify({
                "status": 404,
                "error": "bad request"
            }), 200

@incident_bp.route('/redflags', methods=['POST'])
def create_redflag():
    data = request.get_json()
    if is_valid_request(data):
        location = {"location_long":data['location_long'], "location_lat":data['location_lat']}
        incidents_db.append(Incident(location=location, createdOn=data['createdOn'],\
                    createdBy=data['createdBy'], type=data['type'],\
                    images=data['images'], videos=data['videos'],\
                    comment=data['comment'], date=data['date']))
        return jsonify({
            "status": 200,
            "data":[{
                "id":incidents_db[:-1]['incidentId'],
                "message": "Created red-flag record"}]
        }), 200

    return jsonify({
        "status": 404,
        "error": "bad request"
    }), 200


def is_valid_request(newredflag):
    """
    This function checks for parcel delivery order input if valid.
    """
    if "location" in newredflag and "createdOn" in newredflag and\
     "createdBy" in newredflag and "type" in newredflag and\
      "comment" in newredflag:
        return True
    else:
        return False


@incident_bp.route('/redflags/<int:redFlagId>/location', methods=['PATCH'])
def update_redflag_location(redFlagId):
    for record in incidents_db:
        if record['type'] == redflag:
            data = request.get_json()
            location = {"location_long":data['location_long'], "location_lat":data['location_lat']}
            record.update(location)
            return jsonify({
                "status": 200,
                "data":[{
                    "id":  record['incidentId'],
                    "message": "Updated red-flag record's location"}]
            }), 200

    return jsonify({
        "status": 404,
        "error": "bad request"
    }), 200

@incident_bp.route('/redflags/<int:redFlagId>/comment', methods=['PATCH'])
def update_redflag_comment(redFlagId):
    for record in incidents_db:
        if record['type'] == redflag:
            data = request.get_json()
            comment = data['comment']
            record.update(comment)
            return jsonify({
                "status": 200,
                "data":[{
                    "id":  record['incidentId'],
                    "message": "Updated red-flag record's comment"}]
            }), 200

    return jsonify({
        "status": 404,
        "error": "bad request"
    }), 200


@incident_bp.route('/redflags/<int:redFlagId>/', methods=['DELETE'])
def delete_redflag(redFlagId):
    for record in incidents_db:
        if record['incidentId'] == redFlagId:
            del record
            return jsonify({
                "status": 200,
                "data":[{
                    "id":  record['incidentId'],
                    "message": "red-flag record has been deleted"}]
            }), 200

        return jsonify({
            "status": 404,
            "error": "bad request"
        }), 200
