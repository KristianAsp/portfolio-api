from rest_framework.response import Response
from rest_framework.views import status


def validate_project_request_data(fn):
    def decorated(*args, **kwargs):
        title = args[0].request.data.get("title", "")
        description = args[0].request.data.get("description", "")
        type = args[0].request.data.get("type", None)
        if not title or not description or not type:
            return Response(
                data={
                    "message": "A valid title, description and type are required to add a song"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)
    return decorated

def validate_project_type_request_data(fn):
    def decorated(*args, **kwargs):
        title = args[0].request.data.get("title", "")
        if not title:
            return Response(
                data={
                    "message": "A valid title is required to add or update a project type"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)
    return decorated

def validate_tag_request_data(fn):
    def decorated(*args, **kwargs):
        name = args[0].request.data.get("name", "")
        if not name:
            return Response(
                data = {
                    "message": "A valid name is required to add or update a tag"
                },
                status = status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)
    return decorated