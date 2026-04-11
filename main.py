from models.detector import detect

def main() :
    try :
        detect()
    except KeyboardInterrupt :
        pass


if __name__ == "__main__":
    main()
