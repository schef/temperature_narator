import logic


if __name__ == "__main__":
    print("Boot sequence start")
    logic.init()
    print("Boot sequence end")
    while True:
        logic.loop()