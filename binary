def integer_to_reverse_binary(integer_value):
    binary = ''
    while integer_value > 0:
        binary += str(integer_value % 2)
        integer_value = integer_value // 2
    return binary
def reverse_string(input_string):
    length = len(str(input_string))
    new = ''
    while length > 0:
        new += input_string[length - 1]
        length -= 1
    return new
if __name__ == '__main__':
    num = int(input())
    string = integer_to_reverse_binary(num)
    print(reverse_string(string))
