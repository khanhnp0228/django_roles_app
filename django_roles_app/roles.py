from rolepermissions.roles import AbstractUserRole


class SystemAdmin(AbstractUserRole):
    """
    SystemAdmin: system_admin
    Example: assign_role(<object>, 'system_admin')
    """

    available_permissions = {
        "drop_tables": True,
    }


class Doctor(AbstractUserRole):
    available_permissions = {
        "create_medical_record": True,
    }


class Nurse(AbstractUserRole):
    available_permissions = {
        "edit_patient_file": True,
    }
