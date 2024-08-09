def main():
    name = "David Ruz"
    interests = ["programming", "learning new technologies", "solving problems"]
    message = (
        f"Hello! My name is {name}.\n"
        f"I enjoy {', '.join(interests)}.\n"
        "I'm learning to use Git and GitHub to manage my programming projects."
    )
    print(message)

if __name__ == "__main__":
    main()
