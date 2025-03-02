def count_words_in_file(filename):
    try:
        with open(filename, "r") as file:  
            content = file.read()  
            if not content.strip():  
                raise ValueError("The file is empty.")
            words = content.split()  
            return len(words)  
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{filename}' does not exist.")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

def main():
    print("Welcome to the Word Counter!")
    filename = input("Enter the file name (e.g., example.txt): ").strip()

    try:
        word_count = count_words_in_file(filename)
        print(f"The file '{filename}' contains {word_count} words.")
    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
    