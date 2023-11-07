import transformers


def get_res(message: str):
    pipe = transformers.pipeline(model="Kaludi/Customer-Support-Assistant-V2")

    result = pipe(message)[0]['generated_text']

    response = result.split('.', 1)[0] + '.'

    return response
