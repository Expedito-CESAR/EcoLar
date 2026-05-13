from repositories.user_appliance_repository import (
    create_user_appliance_repository
)

def create_user_appliance_service(
        user_id,
        appliance_id,
        daily_usage,
        monthly_days
):
    
    user_appliance = {
        "user_id": user_id,
        "appliance_id": appliance_id,
        "daily_usage": daily_usage,
        "monthly_days": monthly_days
    }

    create_user_appliance_repository(user_appliance)