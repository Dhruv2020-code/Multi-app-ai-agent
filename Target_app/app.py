def process_user_data(data):
    # Fix: handle missing 'email' key gracefully
    email = data.get("email", None)  # Get email, default to None if missing
    if email is not None:
        email = email.lower()
    return {"user_id": data["id"], "email": email}