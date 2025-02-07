import csv
from users.models import User, UserRoleChange

fields = [
    "Chapter",
    "Office",
    "ConstID",
    "First Name",
    "Middle Name",
    "Last Name",
    "Mobile Phone",
    "School Email",
    "Other Email",
    "Term End",
]


def run():
    all_users = User.objects.all()
    with open("exports/officer_export.csv", "w", newline="") as export_file:
        writer = csv.DictWriter(export_file, fieldnames=fields)
        writer.writeheader()
        for user in all_users:
            roles = user.chapter_officer()
            if roles:
                print(f"Found officer {user}")
                first_role = roles.pop()
                role = (
                    UserRoleChange.get_current_roles(user)
                    .filter(role=first_role)
                    .first()
                )
                writer.writerow(
                    {
                        "Chapter": user.chapter.name,
                        "Office": first_role,
                        "ConstID": user.clean_user_id,
                        "First Name": user.first_name,
                        "Middle Name": "",
                        "Last Name": user.last_name,
                        "Mobile Phone": user.phone_number,
                        "School Email": "",
                        "Other Email": user.email,
                        "Term End": role.end.strftime("%m/%d/%Y"),
                    }
                )
