# 111144445522
# 41442522


# "111144445522"
#
def compresse(string_to_compresse: str):
    last_element = None
    count = 0
    answer = ""
    for element in string_to_compresse:
        if element != last_element:
            if last_element:
                string_to_append = f"{count}:{last_element}"
                last_element = element
                count = 1
                answer = answer + string_to_append
            else:
                count = 1
        else:
            count = count + 1
    return answer


def decompress(decompresed_string: str):
    pass


# - APIs for compression and decompression
# - dockerize it
# - Swagger/postman collection and readme
