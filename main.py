from fastapi import FastAPI

app = FastAPI()


@app.get("/compress")
def compression_api(string_to_compresse: str):
    last_element = None
    count = 0
    answer = ""
    for element in string_to_compresse:
        if element != last_element:
            if last_element:
                string_to_append = f"{count}{last_element}"
                answer = answer + string_to_append
                last_element = element
                count = 1
            else:
                last_element = element
                count = 1
        else:
            count = count + 1
    string_to_append = f"{count}{last_element}"
    answer = answer + string_to_append
    return answer
