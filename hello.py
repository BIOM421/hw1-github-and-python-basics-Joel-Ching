def hello_world():
    return "Hello World!"

def hello_world_n(N):
    return " ".join(["Hello World!"] * N)

if __name__ == "__main__":
    print(hello_world())
    print(hello_world_n(3))

