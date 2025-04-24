def decode_message(encoded_message):
    def dfs(index, path):
        if index == len(encoded_message):
            result.append("".join(path))
            return
        if 1 <= int(encoded_message[index]) <= 9:
            path.append(chr(int(encoded_message[index]) + ord('A') - 1))
            dfs(index + 1, path)
            path.pop()
        if index + 1 < len(encoded_message) and 10 <= int(encoded_message[index:index + 2]) <= 26:
            path.append(chr(int(encoded_message[index:index + 2]) + ord('A') - 1))
            dfs(index + 2, path)
            path.pop()
    result = []
    dfs(0, [])
    return result
def main():
    encoded_message = input("Enter the encoded message: ")

    decoded_messages = decode_message(encoded_message)

    print("\nAll possible decoded messages:")
    for message in decoded_messages:
        print(message)
if __name__ == "__main__":
    main()