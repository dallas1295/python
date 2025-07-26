def build_profile(first, last, **user_info):
    """Buildi a dictionary, containing everything we know about a user given the information provided"""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_profile = build_profile(
    "dallas",
    "sherman",
    location="korea",
    language="python",
    level="learning",
)

print(user_profile)
