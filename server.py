import asyncio
import json
import logging
from itertools import chain
from os import path


from aiofile import async_open
from flask import Flask, jsonify

app = Flask(__name__)

workdir = path.dirname(path.abspath(__file__))


async def read_file(file_name):
    try:
        async with async_open(file_name, 'r') as file:
            return await file.read()
    except Exception:
        logging.exception('something went wrong')


@app.route("/combine", methods=['GET'])
async def combine():

    files_text = await asyncio.gather(*[read_file(f'file_{i}.json') for i in range(1, 4)])
    return jsonify(
        sorted(
            chain.from_iterable(
                json.loads(file_text) for file_text in files_text if file_text is not None
            ),
            key=lambda x: x['id']
        )
    )


app.run(port=8085)

