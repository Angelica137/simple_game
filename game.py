def get_user_input(prompt) -> str:
    return input(prompt)

def intro() -> str:
    return get_user_input("Q: ")


print(intro())