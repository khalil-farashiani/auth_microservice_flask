class ControllerAccessRules:

    _access_rules_roles = {
        "admin": "admin",
        "service": "service",
        "owner": "member:user_id"
    }

    _access_rules_policies = {
        "anonymous": None,
        "admin": [_access_rules_roles["admin"]],
        "all": [
            _access_rules_roles["admin"],
            _access_rules_roles["service"],
            _access_rules_roles["owner"]
        ],
        "admin_or_owner": [
            _access_rules_roles["admin"],
            _access_rules_roles["owner"]
        ],
        "admin_or_service": [
            _access_rules_roles["admin"],
            _access_rules_roles["service"]
        ]
    }

    _controllers_access_rules_roles = {
        "get_users": _access_rules_policies["admin_or_service"],
        "get_user": _access_rules_policies["all"],
        "create_user": _access_rules_policies["anonymous"],
        "update_user": _access_rules_policies["admin_or_owner"],
        "delete_user": _access_rules_policies["admin"]
    }

    def get_controller_rules(f):
        try: 
            return ControllerAccessRules._controllers_access_rules_roles[f]
        except:
            return False
