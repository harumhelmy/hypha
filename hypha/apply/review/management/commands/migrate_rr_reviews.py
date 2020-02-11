from hypha.apply.review.management.commands.migration_review_base import MigrateCommand


class Command(MigrateCommand):
    CONTENT_TYPE = "fund"
    FUND_NAME = "Rapid Response (archive fund)"
    ROUND_NAME = "Rapid Response (archive round)"
    APPLICATION_TYPE = "request"

    STREAMFIELD_MAP = {
        "field_rrr_overall_yes": {
            "id": "cec815a0-fab1-4142-9fc6-71319b054b2a",
            "type": "value",
            "key": "safe_value",
        },
        "field_rrr_overall_no": {
            "id": "6915acf0-9a19-4e73-8d2b-d96e39e3b00e",
            "type": "value",
            "key": "safe_value",
        },
        "field_rrr_objectives_rate": {
            "id": "71bfe95d-89c5-401b-ae7a-778e91d5c8c5",
            "type": "score",
        },
        "field_rrr_capacity_rate": {
            "id": "3aa164c1-4386-4046-997a-a2778e1d894e",
            "type": "score",
        },
        "field_rrr_justification_rate": {
            "id": "7cc12bb6-4c12-48aa-a269-1fd6d725abfe",
            "type": "score",
        },
        "field_rrr_feedback": {
            "id": "comments",
            "type": "value",
            "key": "safe_value",
        },
        "field_rrr_objectives": {
            "id": "38339ef8-8b57-4098-afc8-c3956fdf8333",
            "type": "placeholder",
        },
        "field_rrr_capacity": {
            "id": "f88a4436-cad8-4131-8a32-595c55810606",
            "type": "placeholder",
        },
        "field_rrr_justification": {
            "id": "8d4c9191-ce68-4788-a7f6-66cef5a66288",
            "type": "placeholder",
        },
    }
